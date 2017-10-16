###############################Requests 基本使用##############################
# import requests
# r  =requests.get('https://www.baidu.com/')
# print(type(r))
# print(r.status_code)
# print(type(r.text))
# print(r.text)
# print(r.cookies)

# ###############################Requests GET方法##############################
# import requests
# response = requests.get('http://httpbin.org/get')
# print(response.text)
# ###############################Requests 传入参数data方法##############################
# import requests
# data  ={
#     'name':'pengmeng',
#     'age':'22'
# }
# response = requests.get('http://httpbin.org/get',data)
# print(response.text)
# ###############################Requests 抓取知乎网页##############################
# import requests
# import re
# headers = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0'
# }
# response = requests.get("https://www.zhihu.com/explore",headers = headers)
# pattern  = re.compile('explore-feed.*?question_link.*?>(.*?)</a>',re.S)
# titles = re.findall(pattern,response.text)
# print(titles)
# print(type(titles))
###############################Requests 抓取音视频流保存##############################
# #如果返回结果是图片、音频、视频等文件，Requests 会为我们自动解码成 bytes 类型，即获取字节流数据
# import requests
# response = requests.get("https://github.com/favicon.ico")
# print(response.text,'\n')#字节流转换成str会乱码
# print(response.content,'\n')#b'开头说明response.content内容是bytes数据类型
# with open('F:\PythonProject\PythonFile\github.jpe','wb') as f:
#     f.write(response.content)
# ###############################Requests POST请求判断结果是否正确##############################
# import requests
# response = requests.get("https://github.com/favicon.ico")
# #print('request failed') if not response.status_code == requests.codes.ok else print('request Success')
# exit() if not response.status_code == requests.codes.ok else print('request Success')

# # ###############################Requests 文件上传##############################
# import requests
# files = {'file':open('F:\PythonProject\PythonFile\github.jpe','rb')}
# response = requests.post('http://httpbin.org/post',files=files)
# print(response.text)
# # ###############################Requests 知乎登录cookies#############################################
# import requests
# headers = {
#     'Cookie': 'q_c1=31bb7447a68547c38a3ec853582f724a|1506740203000|1482476896000; d_c0="ACCCnzu0CguPTrnMEtqQRiQ3hmmiba3J1_c=|1482476896"; __utma=51854390.2004248809.1506740162.1506740162.1506740162.1; __utmz=51854390.1506740162.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; r_cap_id="ZmE5ZGQ1MTg0NjUyNGM5Y2E1OGE4YzhmZGQ1NWI5ZDI=|1506740161|1d008edfb1afb68cf40506c949124e9c765fca73"; cap_id="OTQ3NzMzNzEyNzY2NDhlZGJjMWFhNDAwMzBjYzU0ZDI=|1506740161|f81fc934fbcf6cf4b35dab6981033217d1f59dfb"; l_cap_id="OTBmMjRhYmM0ZTQwNDgxNGFjZGFiMmIxY2M5NzYxNzU=|1506740161|8f4f95a400feb46364f8646cf74587a51e7a55fd"; q_c1=31bb7447a68547c38a3ec853582f724a|1504082358000|1482476896000; _zap=339511a2-9a47-48e4-9e8d-aaf6969044f2; aliyungf_tc=AQAAAJoQJxH07gIAw4kS2p6gvrVEMYFU; _xsrf=fd88f5bd786cfdaab864f06e09f2022c; __utmb=51854390.0.10.1506740162; __utmc=51854390; __utmv=51854390.000--|3=entry_date=20161223=1; z_c0="2|1:0|10:1506740201|4:z_c0|92:Mi4xTldfLUFnQUFBQUFBSUlLZk83UUtDeWNBQUFDRUFsVk42WlQyV1FCRHYxejMzM2VHcFpWY0JpMUxTaWIxdnBnRmlR|73db2f4fea0573a63765cd03d4ce42b0a4ee83f7b4fc091be7e2797e463ff12f"; _xsrf=fd88f5bd786cfdaab864f06e09f2022c',
#     'Host': 'www.zhihu.com',
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',
# }
# response = requests.get('https://www.zhihu.com/#signin',headers = headers)
# print(response.text)

# ###############################Requests SSL验证，代理设置，超时设置，身份验证，Prepared REQUEST##############################
# SSL证书验证
#     请求时忽略证书验证就不会报错了response = request.get('http//www.12306.cn', false)
#
# 代理设置
#     对于某些网站，在测试的时候请求几次，能正常获取内容。但是一旦开始大规模爬取，对于大规模且频繁的请求，
#     网站可能会直接登录验证，验证码，甚至直接把IP给封禁掉，此时会需要用到代理
#     若代理需要使用HTTPBasicAuth，可以使用类似http: // user: password @ host:port这样的语法来设置代理。
#     proxies = {
#     'https': 'http://user:password@10.10.1.10:3128/',
#     }
#     requests.get('https://www.taobao.com', proxies=proxies)
#     pip3 install "requests[socks]", 安装Socks库后，就可以使用SOCKS协议代理了
#
# 超时设置
#     r = requests.get('https://www.taobao.com', timeout=1)，这里设置连接和读取时间总和为1秒超时
#     r = requests.get('https://www.taobao.com', timeout=(5, 11))，这里设置connect(连接)和read(读取)分别的超时时间
# 身份认证
#     方式一: r = requests.get('http://localhost:5000', auth=HTTPBasicAuth('username', 'password'))
#     方式二: r = requests.get('http://localhost:5000', auth=('username', 'password'))
#     方式三: OAuth
#     auth = OAuth1('YOUR_APP_KEY', 'YOUR_APP_SECRET', 'USER_OAUTH_TOKEN', 'USER_OAUTH_TOKEN_SECRET')
#     requests.get(url, auth=auth)

#PreparedRequest
from requests import Request,Session
url = 'http://httpbin.org/post'
data = {
    'name': 'germey'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
}
s = Session()
req = Request('POST',url,data=data,headers=headers)
prepped = s.prepare_request(req)
r = s.send(prepped)
print(r.text)











