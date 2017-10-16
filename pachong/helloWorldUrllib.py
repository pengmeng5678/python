#from urllib import request
#def urlopen1():
#    response  = request.urlopen('https://www.python.org')
#    print(response.read().decode('utf-8'))
############################打开基本网址#######################################
# import urllib.request
# def urlopen2():
#     response  = urllib.request.urlopen('https://www.python.org')
#     # print(response.read().decode('utf-8'))
#     print(type(response))
#     print(response.status)
#     print(response.getheaders())
#     print(response.getheader('Server'))
# if __name__=='__main__':
#     # urlopen1()
#     urlopen2()
# ############################data参数#######################################
# #data参数是可选的，如果要添加data，它要是字节流编码格式的内容，即bytes类型，通过bytes可以转化
# #如果传递了这个参数，他的请求方式就不是get而是POST
# import urllib.request
# import urllib.parse
# def datatest():
#     data = bytes(urllib.parse.urlencode({'word':'hello'}),encoding='utf-8')
#     response = urllib.request.urlopen('http://httpbin.org/post',data=data)
#     print(response.read())
# if __name__=='__main__':
#      datatest()
# ############################timeout参数#######################################
# #data参数是可选的，如果要添加data，它要是字节流编码格式的内容，即bytes类型，通过bytes可以转化
# #如果传递了这个参数，他的请求方式就不是get而是POST
# import urllib.request
# import socket
# import urllib.error
# def timeouttest():
#
#     try:
#         response = urllib.request.urlopen('http://httpbin.org/get',timeout=0.1)
#         print(response.read())
#     except urllib.error.URLError as e:
#         if isinstance(e.reason,socket.timeout):
#                 print('TimeOut')
#
# if __name__=='__main__':
#     timeouttest()

# ############################发送请求 request用法#######################################
# #正常请求光用一个url是不够的,如果需要定制很多内容，我们可以构建包含多个参数的Request类型的对象
# from urllib import request,parse
#
# def requesttest():
#     url = 'http://httpbin.org/post'
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
#         'Host': 'httpbin.org'
#     }
#     dict = {
#         'name': 'Germey'
#     }
#     data = bytes(parse.urlencode(dict),encoding='utf-8')
#     req = request.Request(url=url,data=data,headers=headers,method='POST')
#     response  = request.urlopen(req)
#     print(response.read().decode('utf-8'))
# if __name__=='__main__':
#     requesttest()

############################处理异常 HTTPError#######################################
#它是 URLError 的子类，专门用来处理 HTTP 请求错误，比如认证请求失败等等。
# 它有三个属性。
#     code，返回 HTTP Status Code，即状态码，比如 404 网页不存在，500 服务器内部错误等等。
#     reason，同父类一样，返回错误的原因。
#     headers，返回 Request Headers。
from urllib import request,error

def httpErrortest():
    try:
        reason = request.urlopen('http://cuiqingcai.com/index.htm')
    except error.HTTPError as e:
        print(e.code,'\n')
        print(e.reason,'\n')
        print(e.headers)
if __name__=='__main__':
    httpErrortest()