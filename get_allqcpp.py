# coding: utf-8

import requests
from bs4 import BeautifulSoup

def get_html(url):
    """get the content of the url """
    response = requests.get(url)
    response.encoding = 'utf-8'
    return response.text

# 读取汽车品牌link
def get_url_link(html):
    link_list = []
    soup = BeautifulSoup(html, 'html.parser')
    #content = soup.body.find_all("div", class_="line_box")
    content = soup.body.find_all("a")
    for i in content:
        link_list.append(i.get('href'))
    return set(link_list)


# 读取汽车品牌简介
def get_introduction(html):
    soup = BeautifulSoup(html, 'html.parser')
    if soup.find(id="detailBrandStory") is not None:
        content = soup.find(id="detailBrandStory").get_text()
        return content
    return None

#url_car = 'http://car.bitauto.com/audi/'
#html = get_html(url_car)
#content = get_introduction(html)


url_car = 'http://car.bitauto.com/qichepinpai'
html = get_html(url_car)
content = get_url_link(html)
endurl_list = []
for i in content:
    if i is not None and 'car.bitauto.com' in i:
        html = get_html(i)
        print '*'*10 + i + '*'*10
        print get_introduction(html)
        print '-'*30

