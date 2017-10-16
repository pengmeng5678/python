#爬取淘宝的ipad搜索信息
import pymongo
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
# WebDriverWait 对象，它可以指定等待条件，同时指定一个最长等待时间，在这里指定为最长 10 秒。如果在这个时间内成功匹配了等待条件，
# 也就是说页面元素成功加载出来了，那就立即返回相应结果并继续向下执行，否则到了最大等待时间还没有加载出来就直接抛出超时异常
wait = WebDriverWait(browser,10)#显示等待
KEYWORD = 'iPad'
MONGO_URL = 'localhost'
MONGO_DB = 'QA'
MONGO_COLLECTION = 'products'
#连接MongoDB
client = MongoClient()
#指定数据库
db = client[MONGO_DB]
#指定集合
collection = db[MONGO_COLLECTION]

def index_page(page):
    """
    抓取索引页
    :param page: 页码
    :return:
    """
    print('正在爬取第',page,'页')
    try:
        url = 'https://s.taobao.com/search?q='+quote(KEYWORD)
        browser.get(url)
        if page > 1:
            #如果页面大于1，就跳转，否则就等待
            ##mainsrp-pager div.form > input表示mainsrp-pager元素内部的所有div.form元素，且父元素为div.form的所有input元素
            #presence_of_element_located这个条件表示mainsrp-pager div.form > input这个节点出现的意思
            input = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR,'#mainsrp-pager div.form > input')))#输入页码的框
            submit = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR,'#mainsrp-pager div.form > span.btn.J_Submit')))#跳转页码的确认按钮
            input.clear()
            input.send_keys(page)
            submit.click()
        ##mainsrp-pager li.item.active > span是当前的页码节点，即等待页码出现在节点里就表示返回成功了
        #即检测当前高亮的页码节点里是不是我们传过来的页码数，如果是，那就证明页面成功跳转到了这一页，页面跳转成功
        wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager li.item.active > span'), str(page)))
        #.m-itemlist .items .item表示商品信息块，也就是等待商品信息块加载成功并显示
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.m-itemlist .items .item')))
        get_products()
    except TimeoutException:
        index_page(page)
def get_products():
    """
    通过PyQuery提取商品数据
    :return:
    """
    html = browser.page_source
    doc = pq(html)
    items = doc('#mainsrp-itemlist .items .item').items()
    for item in items:
        # print(item)
        if type(item) != None:
            product = {
                'image': item.find('.pic .img').attr('data-src'),
                'price': item.find('.price').text(),
                'deal': item.find('.deal-cnt').text(),
                'title': item.find('.title').text(),
                'shop': item.find('.shop').text(),
                'location': item.find('.location').text()
            }
            print(product)
            save_to_mongo(product)
            save_to_txt(product)
def save_to_txt(product):
    with open('F:\PythonProject\PythonFile\TaoBaoIpad.txt','a',encoding='utf-8') as f:
        f.write(str(product))
        f.write('\n'+'='*50+'\n')

def save_to_mongo(product):
    """
    保存商品信息到mongo
    :param product:
    :return:
    """
    try:
        if collection.insert(product):
            print('保存到MongoDB成功',product)
    except Exception:
        print('保存到MongoDB失败',Exception.__name__)

MAX_PAGE = 5
def main():
    for i in range(1, MAX_PAGE + 1):
        index_page(i)
    browser.close()
if __name__ == '__main__':
    main()

