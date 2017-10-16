from lxml import etree
# text = '''
# <div>
#     <ul>
#          <li class="item-0"><a href="link1.html">first item</a></li>
#          <li class="item-1"><a href="link2.html">second item</a></li>
#          <li class="item-inactive"><a href="link3.html">third item</a></li>
#          <li class="item-1"><a href="link4.html">fourth item</a></li>
#          <li class="item-0"><a href="link5.html">fifth item</a>
#      </ul>
#  </div>
# '''
# html = etree.HTML(text)
# result = etree.tostring(html)
# print(result.decode('utf-8'))

#3输出自动补全HTML标签
# html  = etree.parse('HTMLFile/xpathTest.html',etree.HTMLParser())
# result = etree.tostring(html)
# print(result.decode('utf-8'))

#4匹配所有节点
# html  = etree.parse('HTMLFile/xpathTest.html',etree.HTMLParser())
# result = html.xpath('//*')
# print(result)

#5获取li节点名称
# html  = etree.parse('HTMLFile/xpathTest.html',etree.HTMLParser())
# result = html.xpath('//li')
# print(result)
# print(result[0])

#6获取li节点名称的所有a子节点
# html  = etree.parse('HTMLFile/xpathTest.html',etree.HTMLParser())
# # result = html.xpath('//li/a')   #获取li节点的所有直接a子节点
# # result = html.xpath('//li//a')   #获取li节点的所有a子孙节点
# result = html.xpath('//ul//a')   #获取ul节点的所有a子孙节点
# print(result)
# print(result[0])

# #7已知子节点获取父节点，如<li class="item-1"><a href="link4.html">fourth item</a></li>
# html  = etree.parse('HTMLFile/xpathTest.html',etree.HTMLParser())
# # result = html.xpath('//a[@href="link4.html"]/../@class')   #选择所有节点名称为a,同时属性href的值为link4.html的节点,的所有属性名为class的父节点
# result = html.xpath('//a[@href="link4.html"]/parent::*/@class') #用parent::也可以表示以上规则
# print(result)

# #8属性匹配
# html  = etree.parse('HTMLFile/xpathTest.html',etree.HTMLParser())
# result = html.xpath('//li[@class="item-1"]')   #选择所有节点名称为li,同时属性class的值为item-1的节点
# print(result)

#9获取节点内部的文本
# # <li class="item-0"><a href="link1.html">first item</a></li>
# # <li class="item-0"><a href="link5.html">fifth item</a>
# # </li>
# html  = etree.parse('HTMLFile/xpathTest.html',etree.HTMLParser())
# # result = html.xpath('//li[@class="item-0"]/text()')   #选择所有节点名称为li,同时属性class的值为item-0的节点下的文本
# #这里只会获取到一个换行符，因为是获取的item-0的直接子节点，这个直接子节点只有一个换行符
# #所以可以改为以下两种方式获取节点文本
# result = html.xpath('//li[@class="item-0"]//text()')    #输出['first item', 'fifth item', '\r\n     ']，即所有节点名称为li,同时属性class的值为item-0的所有节点下的文本
# # result = html.xpath('//li[@class="item-0"]/a/text()')     #['first item', 'fifth item']，即所有节点名称为li/a,同时属性class的值为item-0的直接子节点下的文本
# print(result)

#10获取节点内部的属性
# html  = etree.parse('HTMLFile/xpathTest.html',etree.HTMLParser())
# result = html.xpath('//li/a/@href') #获取所有 li 节点下所有 a 节点的 href 属性
# print(result)

#11属性多值匹配,即匹配含有多个属性值中的一个
# text = '''
# <li class="li li-first"><a href="link.html">first item</a></li>
# '''
# html  = etree.HTML(text)
# #这里HTML文本中的li节点的class属性有两个值li和li-first,无法用之前的规则匹配,需要用到contains函数
# # result = html.xpath('//li[@class="li"]/a/text()')   #错误示例
# result = html.xpath('//li[contains(@class,"li")]/a/text()')
# print(result)

#12多属性匹配,即含有多个属性值。同时匹配
# text = '''
# <li class="li li-first" name="item"><a href="link.html">first item</a></li>
# '''
# html  = etree.HTML(text)
# #这里HTML文本中的li节点的class属性有两个值li和li-first,无法用之前的规则匹配,需要用到contains函数
# # result = html.xpath('//li[@class="li"]/a/text()') #错误示例
# result = html.xpath('//li[contains(@class,"li") and @name="item"]/a/text()')
# print(result)

#13按序选择
# text = '''
# <div>
#     <ul>
#          <li class="item-0"><a href="link1.html">first item</a></li>
#          <li class="item-1"><a href="link2.html">second item</a></li>
#          <li class="item-inactive"><a href="link3.html">third item</a></li>
#          <li class="item-1"><a href="link4.html">fourth item</a></li>
#          <li class="item-0"><a href="link5.html">fifth item</a>
#      </ul>
#  </div>
# '''
# html = etree.HTML(text)
# result = html.xpath('//li[1]/a/text()')     #序号是从1开始的
# print(result)
# result = html.xpath('//li[last()]/a/text()')
# print(result)
#
# result = html.xpath('//li[last()-1]/a/text()')
# print(result)
#
# result = html.xpath('//li[position()<3]/a/text()')
# print(result)
######################################测试使用###############################
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
html = etree.HTML(html)
result = html.xpath('//ul//li//p//a/@href')
print(result)