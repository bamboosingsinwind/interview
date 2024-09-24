import requests
from PIL import Image
import os
import io
# 获取图片的url
def get_image_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    else:
        print('获取图片失败')

# 保存图片
def save_image(image_content, image_name):
    image = Image.open(io.BytesIO(image_content))
    image.save(image_name)