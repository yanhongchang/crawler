# coding: utf-8

import requests
from bs4 import BeautifulSoup

def get_html(url):
    """get the content of the url """
    response = requests.get(url)
    response.encoding = 'utf-8'
    return response.text

# 读取汽车品牌简介
def get_introduction(html):
    soup = BeautifulSoup(html, 'html.parser')
    content = soup.find(id="detailBrandStory").get_text()
    return content

url_car = 'http://car.bitauto.com/audi/'
html = get_html(url_car)
content = get_introduction(html)
print content
