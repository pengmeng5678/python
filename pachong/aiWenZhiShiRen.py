from lxml import etree
from pymongo import MongoClient
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pyquery import PyQuery as pq
from urllib.parse import quote
# browser = webdriver.Chrome()

#Chrome Headless模式，也就是无界面模式，这样爬取的时候就不会弹出浏览器了
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=chrome_options)
wait = WebDriverWait(browser,10)#显示等待

CollectionName = [' ','neike','jingShenXinLiKe','waiKe','zhengXingMeiRong','erKe','zhongLiuKe','nanKe','chuanRanKe','wuGuanKe','piFuKe','renTiChangeShi','fuChanKe']
MONGO_URL = 'localhost'
MONGO_DB = 'QA_data'
#连接MongoDB
client = MongoClient()
#指定数据库
db = client[MONGO_DB]
#指定集合
collection = db['aiWen']

MainPageUrl = 'http://iask.sina.com.cn/c/79.html'
BaseUrl = 'http://iask.sina.com.cn'
def index_page(urlIndex,index):
    """
    当前页面的问答
    :return:
    """
    try:
        url = BaseUrl+quote(urlIndex)
        print('正在爬取的网址:',url)
        browser.get(url)
        # 等待问题和答案块显示出来
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.w680 .good_point .good_answer')))
        get_QA_text(index)
    except TimeoutException:
        print('没有好评答案的网址:',urlIndex)
def get_QA_text(index):
    html = browser.page_source
    doc = pq(html)
    mainClassfy = CollectionName[index]
    classfy = doc('.breadcast.pw.pw-v .breadcast-fl.no-fl').text()
    question = doc('.question_wrapper .question_text').text()
    answer = doc('.good_point .good_answer .answer_text').text()
    # print('当前问题分类：',classfy)
    # print('抓取的问题：',question)
    # print('抓取的答案：',answer)
    QA_data = {
        'mainClassfy':mainClassfy,
        'classfy':classfy,
        'question':question,
        'answer':answer
    }
    save_to_mongo(QA_data,index)

def save_to_mongo(qadata,index):
    """
    保存问答数据到mongo
    :param qaInfo:
    :return:
    """
    try:
        if collection.insert(qadata):
            print('保存到MongoDB成功',qadata)
    except Exception:
        print('保存到MongoDB失败',Exception.__name__)
def process_main_page(mainPageUrl,index):
    browser.get(mainPageUrl)
    # 等待内科块显示出来
    currentTab = '#J_tabs_0'+str(index)
    print('main_page currentTab = ',currentTab)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, currentTab+'.channel-list.mt30 .channel-list-con.cf.current')))
    # wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#J_tabs_01.channel-list.mt30 .channel-list-con.cf.current')))
    html = browser.page_source
    doc = pq(html)
    uls = doc(currentTab+' .channel-list-con').items()   #第一个tabs对应的所有html
    # uls = doc('#J_tabs_01 .channel-list-con').items()   #第一个tabs对应的所有html

    for ul in uls:#一个uls表示所有的内科，一个ul表示一个小科(如内分泌科，呼吸内科...)
        # print(ul)
        # print(type(ul))
        # TODO#这里使用PyQuery解析出来的PyQuery对象,不知道为什么ul标签中包含了xmls属性后通过find('li')拿不到数据,所以我才用了Xpath解析内部的数据
        mystr = str(ul)#这里转换成Str后便于用XPath再次解析
        # print(type(mystr))
        # print(mystr)
        html = etree.HTML(mystr)
        hrefs = html.xpath('//ul//li//p//a/@href')#解析出tab1所有的链接,这里是一个list,表示一个小科的所有链接
        print('当前ul的所有hrefs',hrefs)
        for href in hrefs:
            print(href)
            index_page(href,index)

if __name__ == '__main__':
    for index in range(1,13):#12种大分类，tabs,如内科、外科...
        print('当前爬取的问题分类：',CollectionName[index])
        process_main_page(MainPageUrl,index)
    # url = '/b/6fQYl2GDt5h.html'
    # index_page(url)
    browser.close()