import requests
from bs4 import BeautifulSoup
import os

# 获取网页源代码
url = 'https://keyassets.timeincuk.net/inspirewp/live/wp-content/uploads/sites/8/2019/12/GettyImages-169448287.jpg'
response = requests.get(url)
# 获取网页源代码
html = response.text
# 解析网页源代码
soup = BeautifulSoup(html, 'html.parser')
# 获取图片的src标签
img_src = soup.find('img')['src']
# 保存图片
with open('img.jpg', 'wb') as f:
    f.write(requests.get(img_src).content)
# 保存图片
os.rename('img.jpg', 'img.png')