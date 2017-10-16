from urllib.parse import  urlencode
from multiprocessing.pool import Pool
import os
from hashlib import md5
import requests
base_url = 'http://www.toutiao.com/search_content/?'
def get_page(offset):
    params = {
        'offset': offset,
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': '20',
        'cur_tab': '1',
    }
    url = base_url +urlencode(params)
    response = requests.get(url)
    try:
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError:
        return None
def get_images(json):
    if json.get('data'):
        for item in json.get('data'):
            title = item.get('title')
            images = item.get('image_detail')
            print(type(images))
            if  isinstance(images,list):
                for image in images:
                    yield {
                        'image':image.get('url'),
                        'title':title
                    }
def save_image(item):
    if not os.path.exists('F:/PythonProject/PythonFile/touTiaoJiePai_Ajax/'+item.get('title')):
        os.mkdir('F:/PythonProject/PythonFile/touTiaoJiePai_Ajax/'+item.get('title'))
    try:
        response = requests.get(item.get('image'))
        print('response = ',response.content)
        if response.status_code  == 200:
            file_path = '{0}/{1}.{2}'.format('F:/PythonProject/PythonFile/touTiaoJiePai_Ajax/'+item.get('title'),md5(response.content).hexdigest(),'jpg')
            if not os.path.exists(file_path):
                with open(file_path,'wb') as f:
                    f.write(response.content)
            else:
                print('Already Downloaded',file_path)
        else:
            print('response.status_code != 200')
    except requests.ConnectionError:
        print('Failed to Save Image')

def main(offset):
    json = get_page(offset)
    for item in get_images(json):
        print(item)
        save_image(item)

GROUP_START=1
GROUP_END=20
if __name__ == '__main__':
    pool = Pool()
    groups = ([x * 20 for x in range(GROUP_START, GROUP_END + 1)])
    pool.map(main,groups)   #把元组中的每一个数作用在main函数上
    pool.close()
    pool.join()