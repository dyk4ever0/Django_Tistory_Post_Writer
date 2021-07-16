import socket
import requests
import json
from bs4 import BeautifulSoup

from dotenv import load_dotenv

load_dotenv(verbose=True)
import os

origin = 'out'
output_type = 'json'


def json_parsing(response_json):
    json_text = json.dumps(response_json, indent=4, ensure_ascii=False)
    return json_text



def blog_info():

    url = 'https://www.tistory.com/apis/blog/info'
    data = {'access_token': os.getenv("TI_ACCESS_TOKEN"), 'output': output_type}
    res = requests.get(url, params=data)
    print(res.url)
    if res.status_code == 200:
        json_text = json_parsing(res.json())
        print(json_text)
    else:
        json_text = json_parsing(res.json())
        print(json_text)




def blog_category_list(blog_name):

    url = 'https://www.tistory.com/apis/category/list'
    data = {'access_token': os.getenv("TI_ACCESS_TOKEN"), 'output': output_type, 'blogName': blog_name}
    res = requests.get(url, params=data)

    if res.status_code == 200:
        json_text = json_parsing(res.json())
        print(json_text)
    else:
        json_text = json_parsing(res.json())
        print(json_text)


def blog_list(blog_name, page):
    url = 'https://www.tistory.com/apis/post/list'

    data = {'access_token': os.getenv("TI_ACCESS_TOKEN"), 'output': output_type, 'blogName': blog_name, 'page': page}
    res = requests.get(url, params=data)
    print(res.url)
    if res.status_code == 200:
        json_text = json_parsing(res.json())
        print(json_text)
    else:
        json_text = json_parsing(res.json())
        print(json_text)



def blog_read(blog_name, post_id):
    url = 'https://www.tistory.com/apis/post/read'

    data = {'access_token': os.getenv("TI_ACCESS_TOKEN"), 'output': output_type, 'blogName': blog_name,
            'postId': post_id}
    res = requests.get(url, params=data)
    print(res.url)
    if res.status_code == 200:
        json_text = json_parsing(res.json())
        print(json_text)
    else:
        json_text = json_parsing(res.json())
        print(json_text)



def blog_write(blog_name, category_id, title, content, tag):
    url = 'https://www.tistory.com/apis/post/write'
    visibility = 3
    published = ''
    slogan = ''
    acceptComment = 1
    password = ''

    data = {'access_token': os.getenv("TI_ACCESS_TOKEN"), 'output': output_type, 'blogName': blog_name, 'title': title,
            'content': content, 'visibility': visibility, 'category': category_id, 'published': published,
            'slogan': slogan, 'tag': tag, 'acceptComment': acceptComment, 'password': password}
    res = requests.post(url, data=data)
    print(res.url)
    if res.status_code == 200:
        json_text = json_parsing(res.json())
        print(json_text)
    else:
        json_text = json_parsing(res.json())
        print(json_text)


if __name__ == '__main__':
    # utils.check_folder(origin)

    blog_info()

    blog_category_list("floatingavocadoseed")