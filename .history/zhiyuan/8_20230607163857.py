import requests
from bs4 import BeautifulSoup
import re
import time
import random
import os

# 定义一个函数，用来获取网页的源代码
def get_html(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.ConnectionError:
        return None

# 定义一个函数，用来获取网页的标题
def get_title(html):
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.title.string
    return title

# 定义一个函数，用来获取网页的正文
def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    content = soup.find('div', class_='article-body')
    return content
print(get_html("https://blog.csdn.net/qq_34451909/article/details/110233820"))