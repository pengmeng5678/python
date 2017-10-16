#Selenium 是一个自动化测试工具，利用它我们可以驱动浏览器执行特定的动作，如点击、下拉等等操作，
# 同时还可以获取浏览器当前呈现的页面的源代码，做到可见即可爬。对于一些 JavaScript 动态渲染的页面来说，此种抓取方式非常有效

#############使用谷歌浏览器打开百度，从搜索框搜索Python后获取新页面的网址，cookies，网页源码数据##################
import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
# try:
#     browser.get('https://www.baidu.com')
#     input = browser.find_element_by_id('kw')
#     input.send_keys('Python')
#     input.send_keys(Keys.ENTER)
#     wait = WebDriverWait(browser,10)
#     wait.until(EC.presence_of_element_located((By.ID,'content_left')))
#     print(browser.current_url)
#     print(browser.get_cookies())
#     print(browser.page_source)
# finally:
#     browser.close()
###################################详细使用#######################################
#3########################################声明浏览器对象##########################################
browser = webdriver.Chrome()
# browser = webdriver.Firefox()
# browser = webdriver.Edge()
# browser = webdriver.PhantomJS()
# browser = webdriver.Safari()
#4########################################访问页面##########################################
# browser.get('https://www.taobao.com')
# print(browser.page_source)
#5########################################查找节点##########################################
#模拟点击和填充表单的时候，或者输入文字需要知道输入框在哪，所以需要查找节点
#单个节点
# input_first = browser.find_element_by_id('q')
# input_first1 = browser.find_element(By.ID, 'q')#通过ID查找的另一种方式
# print(input_first1)
# input_second = browser.find_element_by_css_selector('#q')
# input_third = browser.find_element_by_xpath('//*[@id="q"]')
# print(input_first ,'\n',input_second,'\n', input_third)
# browser.close()

#多个节点(爬取左侧的导航栏节点)
# browser.get('https://www.taobao.com')
# lis = browser.find_element_by_css_selector('.service-bd li')#单个节点是WebElement类型
# # lis = browser.find_elements_by_css_selector('.service-bd li')#所有节点
# lis1 = browser.find_elements(By.CSS_SELECTOR,'.service-bd li')#另一种方式获取所有节点
# print(type(lis))
# print(lis)
# print(lis1)
#6########################################节点交互##########################################
#模拟浏览器执行一些操作，如输入文字send_keys,清空文字clear,还有按钮点击click
# input = browser.find_element_by_id('q')
# input.send_keys('iPhone')
# time.sleep(1)
# input.clear()
# input.send_keys('iPad')
# button = browser.find_element_by_class_name('btn-search')
# button.click()
    #更多操作方式http://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.remote.webelement
#7########################################动作链##########################################
# url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
# browser.get(url)
# browser.switch_to.frame('iframeResult')
# source = browser.find_element_by_css_selector('#draggable')
# target = browser.find_element_by_css_selector('#droppable')
# actions = ActionChains(browser)
# actions.drag_and_drop(source, target)
# actions.perform()
#更多操作链http://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.common.action_chains

#8########################################执行JavaScript##########################################
# browser.get('https://www.zhihu.com/explore')
# browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
# browser.execute_script('alert("To Bottom")')
#9#######################获取节点信息(获取属性和文本、获取ID、位置、标签名、大小)###############################
#获取属性
url = 'https://www.zhihu.com/explore'
browser.get(url)
logo = browser.find_element_by_id('zh-top-link-logo')
print(logo)
print(logo.get_attribute('class'))
#获取文本,获取ID、位置、标签名、大小
logo1 = browser.find_element_by_id('zh-top-link-logo')
print(logo1.text)
print(logo1.id)
print(logo1.location)
print(logo1.tag_name)
print(logo1.size)
# browser.close()
#10#######################################切换Frame###############################
#11#######################################延迟等待(隐式等待和显示等待)###############################
#隐式等待
# browser.implicitly_wait(10)
# browser.get('https://www.zhihu.com/explore')
# input = browser.find_element_by_class_name('zu-top-add-question')
# print(input)
#显示等待
#presence_of_element_located这个条件表示节点出现的意思，其参数就是节点的定位元组
#element_to_be_clickable这个条件表示如果10秒内它是可点击的也就是成功加载出来了，那就返回该节点，否则抛出异常
# browser.get('https://www.taobao.com/')
# wait = WebDriverWait(browser, 10)#指定好最长等待时间
# input = wait.until(EC.presence_of_element_located((By.ID, 'q')))
# button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
# print(input, button)
#12#######################################前进后退###############################
# browser.get('https://www.baidu.com/')
# browser.get('https://www.taobao.com/')
# browser.back()
# time.sleep(1)
# browser.forward()
# browser.close()
#13#######################################Cookies###############################
# browser = webdriver.Chrome()
# browser.get('https://www.zhihu.com/explore')
# print(browser.get_cookies())
# browser.add_cookie({'name': 'name', 'domain': 'www.zhihu.com', 'value': 'germey'})
# print(browser.get_cookies())
# browser.delete_all_cookies()
# print(browser.get_cookies())
#14#######################################选项卡管理###############################
# browser.get('https://www.baidu.com')
# browser.execute_script('window.open()')
# print(browser.window_handles)
# browser.switch_to_window(browser.window_handles[1])
# browser.get('https://www.taobao.com')
# time.sleep(1)
# browser.switch_to_window(browser.window_handles[0])
# time.sleep(2)
# browser.execute_script('window.close()')
# print("关闭当前页面")
#15#######################################异常处理###############################
# try:
#     browser.get('https://www.baidu.com')
# except TimeoutException:
#     print('Time Out')
# try:
#     browser.find_element_by_id('hello')
# except NoSuchElementException:
#     print('No Element')
# finally:
#     browser.close()
