from pyquery import PyQuery as pq
from selenium import webdriver
################1.初始化：可以传入HTML、URL、文件名、字符串###############################

# html = '''
# <div>
#     <ul>
#          <li class="item-0">first item</li>
#          <li class="item-1"><a href="link2.html">second item</a></li>
#          <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
#          <li class="item-1 active"><a href="link4.html">fourth item</a></li>
#          <li class="item-0"><a href="link5.html">fifth item</a></li>
#      </ul>
#  </div>
# '''
# #HTML初始化
# doc = pq(html)
# print(doc('li'))
# #URL初始化
# doc1 = pq(url = "http://cuiqingcai.com")
# print(doc1('title'))
# #文件初始化
# doc2 = pq(filename = 'xpathTest.html')
# print(doc2('li'))
###############################2.基本CSS选择器###############################
# html = '''
# <div class="wrap">
#     <div id="container">
#         <ul class="list">
#              <li class="item-0">first item</li>
#              <li class="item-1"><a href="link2.html">second item</a></li>
#              <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
#              <li class="item-1 active"><a href="link4.html">fourth item</a></li>
#              <li class="item-0"><a href="link5.html">fifth item</a></li>
#          </ul>
#      </div>
#  </div>
# '''
# # doc = pq(html)
# # print(doc('#container .list li'))
# # print(type(doc('#container .list li')))
# ###############################3.查找节点###############################
# #子节点
# doc = pq(html)
# items = doc('.list')
# # print(items)
# lis = items.find('li')
# # print(lis)
# #直接父节点用parent,所有父节点用parents
# # print(items.parent())
# # print(type(items.parents()))
# # print(items.parents())
# #获取某个父节点
# # print(items.parents('.wrap'))
# #兄弟节点
# li = doc('.list .item-0.active')
# print(li.siblings())

###############################4.获取信息###############################
#获取属性
# html = '''
# <div class="wrap">
#     <div id="container">
#         <ul class="list">
#              <li class="item-0">first item</li>
#              <li class="item-1"><a href="link2.html">second item</a></li>
#              <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
#              <li class="item-1 active"><a href="link4.html">fourth item</a></li>
#              <li class="item-0"><a href="link5.html">fifth item</a></li>
#          </ul>
#      </div>
#  </div>
# '''
# doc = pq(html)
# a = doc('.item-0.active a')
# # print(a,type(a))
# # print(a.attr('href'))
# # print(a.attr.href)  #与上面结果一致
# #获取文本
# # print(a)
# # print(a.text())
# li = doc('.item-1.active')
# print(li)
# print(li.text())

###############################5.节点操作###############################
# html = '''
# <div class="wrap">
#     <div id="container">
#         <ul class="list">
#              <li class="item-0">first item</li>
#              <li class="item-1"><a href="link2.html">second item</a></li>
#              <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
#              <li class="item-1 active"><a href="link4.html">fourth item</a></li>
#              <li class="item-0"><a href="link5.html">fifth item</a></li>
#          </ul>
#      </div>
#  </div>
# '''
#class操作
# doc = pq(html)
# li = doc('.item-0.active')
# print(li)
# li.remove_class('active')
# print(li)
# li.add_class('active')
# print(li)

#attr、text、html操作
# doc = pq(html)
# li = doc('.item-0.active')
# li.attr('name','link')  #增加一个属性
# print(li)
#
# li.text('change text')
# print(li)   #改变文本
#
# li.html('hahaha')   #text() 和 html() 方法如果不传参数是获取节点内纯文本和 HTML 文本，如果传入参数则是进行赋值
# print(li)

#remove
# html = '''
# <div class="wrap">
#     Hello, World
#     <p>This is a paragraph.</p>
#  </div>
# '''
# doc = pq(html)
# wrap = doc('')

###############################案例测试#####################
html = '''
<ul xmlns="http://www.w3.org/1999/xhtml" class="channel-list-con cf">
		            	 <li><p><a href="/b/6hTLEMZXmA3.html" target="_blank">混合性结缔组织病有哪些临床表现？</a></p></li>
		                 <li><p><a href="/b/6eRZhl2LXzt.html" target="_blank">混合性结缔组织病是什么？</a></p></li>
		                 <li><p><a href="/b/6ezFstfY9vR.html" target="_blank">肌无力程度如何判断？</a></p></li>
		                 <li><p><a href="/b/6d64gNatyll.html" target="_blank">肌无力患者会有哪些临床表现？</a></p></li>
		                 <li><p><a href="/b/6feTdWB1Yuf.html" target="_blank">1975年B0han和Peter将PM/DM分为哪几类？</a></p></li>
		                 <li><p><a href="/b/6d1udwiJZph.html" target="_blank">多发性肌炎和皮肌炎是种什么病？</a></p></li>
		                 <li><p><a href="/b/6dS6IL1VuD9.html" target="_blank">系统性硬化病怎么治疗？</a></p></li>
		                 <li><p><a href="/b/6jth3YJ7KTV.html" target="_blank">系统性硬化病的诊断要点是什么？</a></p></li>
		                 <li><p><a href="/b/6hbigFymeo3.html" target="_blank">系统性硬化 有何临床表现？</a></p></li>
		                 <li><p><a href="/b/6e4VOTUZe9Z.html" target="_blank">系统性硬化有哪几种分类？</a></p></li>
		                 <li><p><a href="/b/6f73bBm1bMn.html" target="_blank">系统性硬化是一种什么病？</a></p></li>
		                 <li><p><a href="/b/6dZTwcozlz5.html" target="_blank">植物药制剂有什么不良反应？</a></p></li>
		                 <li><p><a href="/b/6gSvVM0qaEP.html" target="_blank">银屑病关节炎 有何症状和体征？</a></p></li>
		                 <li><p><a href="/b/6dVjF8Fsxcv.html" target="_blank">银屑病关节炎有哪些临床表现？</a></p></li>
		                 <li><p><a href="/b/6evX9Uc4V51.html" target="_blank">银屑病关节炎是种什么病？</a></p></li>
		                 <li><p><a href="/b/6gEMapbfyIP.html" target="_blank">肠病性关节炎是什么？</a></p></li>
		                 <li><p><a href="/b/6iuOPnU6ft9.html" target="_blank">赖特综合征如何治疗啊？</a></p></li>
		                 <li><p><a href="/b/6hjU9R6M6OT.html" target="_blank">赖特综合征发病有什么临床表现？</a></p></li>
		                 <li><p><a href="/b/6c9iNP7NeH1.html" target="_blank">赖特综合征的发病与哪些因素有关？</a></p></li>
		                 <li><p><a href="/b/6dxRLPd4jML.html" target="_blank">赖特综合征有哪几种形式？</a></p></li>
		                 </ul>
'''
doc = pq(html)
# print(doc('.channel-list-con'))
print('doc',doc.find('a'))
print('li',doc('li'))
# doc1 = pq(html)
# lis = doc1('li')
# print(lis)