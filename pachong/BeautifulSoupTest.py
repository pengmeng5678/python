from bs4 import BeautifulSoup
import re
print('————————————————————华丽的分割线下面是基本使用——————————————————\n')
# html = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>
# <p class="story">...</p>
# """
#
# #节点选择器与基本使用
# soup = BeautifulSoup(html, 'lxml')
# print(soup.title)
# print(type(soup.title))
# print(soup.title.string)
# print(soup.head)
# print(soup.p,'\n')
# print(soup.prettify())
#
# #提取信息
# # print(soup.title.name)        #获取名称，选取title节点，调用name属性就可以获取节点名称
# print(soup.p.attrs)             #获取属性，返回一个字典{'name': 'dromouse', 'class': ['title']}
# print(soup.p.attrs['name'])         #获取key为name的值
# print(soup.p.attrs['class'])        #获取key为class的值
# print(soup.p['name'])               #简写，获取key为name的值，返回dromouse
# print(soup.p['class'])              #简写，获取key为class的值，返回['title']
# print(soup.p.string)            #获取内容，返回The Dormouse's story
#
# #嵌套选择
# # 我们知道每一个返回结果都是 bs4.element.Tag 类型，
# # 它同样可以继续调用节点进行下一步的选择，比如我们获取了 head 节点元素，我们可以继续调用 head 来选取其内部的 head 节点元素。
# print(soup.head.title)
# print(type(soup.head.title))
# print(soup.head.title.string)
print('————————————————————华丽的分割线下面是节点选择器——————————————————\n')
# html = """
# <html>
#     <head>
#         <title>The Dormouse's story</title>
#     </head>
#     <body>
#         <p class="story">
#             Once upon a time there were three little sisters; and their names were
#             <a href="http://example.com/elsie" class="sister" id="link1">
#                 <span>Elsie</span>
#             </a>
#             <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
#             and
#             <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
#             and they lived at the bottom of a well.
#         </p>
#         <p class="story">...</p>
# """
# soup = BeautifulSoup(html,'lxml')
# # print(soup.p.contents)    #contents 属性得到的结果是直接子节点的列表
# #关联选择
# #子节点和子孙节点用child属性
# print(soup.p.descendants)   #得到所有的子孙节点,返回一个generator
# # for i,child in enumerate(soup.p.descendants):
# #     print(i,child)
#
# #父节点和祖先节点用parent属性
# #在这里我们选择的是第一个 a 节点的父节点元素，很明显它的父节点是 p 节点，输出结果便是 p 节点及其内部的内容。
# #这里输出的仅仅是 a 节点的直接父节点，而没有再向外寻找父节点的祖先节点，如果我们要想获取所有的祖先节点，可以调用 parents 属性
# print(soup.a.parent)
# # print(list(enumerate(soup.a.parents)))

#兄弟节点
# html = """
# <html>
#     <body>
#         <p class="story">
#             Once upon a time there were three little sisters; and their names were
#             <a href="http://example.com/elsie" class="sister" id="link1">
#                 <span>Elsie</span>
#             </a>
#             Hello
#             <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
#             and
#             <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
#             and they lived at the bottom of a well.
#         </p>
# """
# soup = BeautifulSoup(html,'lxml')
# print('Next Sibling',soup.a.next_sibling)
# print('prev sibling',soup.a.previous_sibling)
# print('Next siblings',list(enumerate(soup.a.next_siblings)))
# print('prev siblings',list(enumerate(soup.a.previous_siblings)))

#提取信息
# print('Next Sibling:')
# print(type(soup.a.next_sibling))
# print(soup.a.next_sibling)
# print(soup.a.next_sibling.string)
# print('Parent:')
# print(type(soup.a.parents))
# print(list(soup.a.parents)[0])
# print(list(soup.a.parents)[0].attrs['class'])
print('————————————————————华丽的分割线下面是方法选择器——————————————————\n')
html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
from bs4 import BeautifulSoup
#根据name节点名查询
soup = BeautifulSoup(html, 'lxml')
# print(soup.find_all(name='ul'))
# print(type(soup.find_all(name='ul')[0]))    #返回的都是TAG类型，所以可以嵌套查询
#
# for ul in soup.find_all(name='ul'):
#     print(ul.find_all(name='li'))

#根据attrs属性查询
#查询的时候传入的是 attrs 参数，参数的类型是字典类型
# print(soup.find_all(attrs={'class':'panel-body'}))
# print(soup.find_all(attrs={'id':'list-2'}))   #包含的内容就是符合 id 为 list-2 的所有节点

#简写形式也可以这样写，而对于class来说，class是一个关键字，需要再后面加一个下划线
# print(soup.find_all(id='list-2'))
# print(soup.find_all(class_='element'))

#text参数用来匹配节点的文本,匹配的内容可以是文本，也可以是正则表达式对象
# print(soup.find_all(text=re.compile('oo')))
print(soup.find_all(text="Foo"))

#find 方法返回的是单个元素，也就是第一个匹配的元素，而 find_all() 返回的是所有匹配的元素组成的列表
print(soup.find(name='ul'))