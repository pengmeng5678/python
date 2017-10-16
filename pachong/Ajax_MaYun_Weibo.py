from urllib.parse import  urlencode
from pyquery import PyQuery as pq
from pymongo import MongoClient
from bson.objectid import ObjectId
import requests
base_url = 'https://m.weibo.cn/api/container/getIndex?'
headers = {
    'Host':'m.weibo.cn',
    'Referer':'https://m.weibo.cn/u/2145291155',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'X-Requested-With':'XMLHttpRequest'
}
client = MongoClient()  #连接MongoDB
db = client['weibo']    #指定数据库
collection = db['weibo']#指定集合
max_page = 14
def get_page(page):
    paras = {
        'type':'uid',
        'value':'2145291155',
        'containerid':'1076032145291155',
        'page':page,
    }
    url = base_url+urlencode(paras)
    response = requests.get(url,headers = headers)
    try:
        if response.status_code == 200:
            return response.json()
        else:
            print(response.status_code,response.text,response.content)
    except requests.ConnectionError as e:
        print('Error',e.args)

def parse_page(json):
    items = json.get('cards')
    for item in items:
        item = item.get('mblog')
        weibo = {}
        weibo['id'] = item.get('id')
        # weibo['text'] = item.get('text')
        #'天天有这样豪宅、豪车说是我的，看多了我自己都快信啦……拜托这些“资产”背后的策划公司也能真给我一些啊？
        # <span class="url-icon"><img src="//h5.sinaimg.cn/m/emoticon/icon/default/d_shiwang-775c6c63ae.png" style="width:1em;height:1em;" alt="[失望]">
        weibo['text'] = pq(item.get('text')).text() #去除多余样式
        weibo['attitudes_count'] = item.get('attitudes_count')
        weibo['comments_count'] = item.get('comments_count')
        weibo['reposts_count'] = item.get('reposts_count')
        print('weibo',weibo)
        yield weibo
def save_to_mongo(result):
    save_result =  collection.insert(result)
    print('Save to Mongo result:',save_result)
if __name__ == '__main__':
    for page in range(1,15):
        json = get_page(page)
        print(json,'/n')
        results = parse_page(json)
        for result in results:
            print(result)
            save_to_mongo(result)
    result = collection.find_one({'attitudes_count':1610})
    # result = collection.find_one({'_id': ObjectId('59dc68b9bb033b19b80116d5')})
    print(type(result))
    print(result)



