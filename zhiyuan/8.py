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

# 获取图片的url
url = 'https://img.zcool.cn/community/01d4435bc4974ea8012099c800e70d.jpg@1280w_1l_2o_100sh.jpg'
image_content = get_image_url(url)
image_name = 'zcool.jpg'
save_image(image_content, image_name)