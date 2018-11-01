

import re
import time
from lxml import etree
from selenium.common.exceptions import TimeoutException

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote
import json
import requests


# 打开浏览器
browser = webdriver.Chrome()
# 设置浏览器大小
browser.set_window_size(1200, 700)
# 设置超时时间
wait = WebDriverWait(browser,20)

KEYWORDS = '连衣裙'

num = 1


def index_page(nums):

    try:
        time.sleep(1)
        url = 'https://www.yohobuy.com/girls-new/ci2-gd2.html?order=s_t_desc&page='+str(nums)+''
        browser.get(url)
        browser.execute_script('window.scrollTo(0, document.body.scrollHeight/8)')
        time.sleep(2)
        browser.execute_script('window.scrollTo(0,2*document.body.scrollHeight/8)')
        time.sleep(2)
        browser.execute_script('window.scrollTo(0,3*document.body.scrollHeight/8)')
        time.sleep(2)
        browser.execute_script('window.scrollTo(0,4*document.body.scrollHeight/8)')
        time.sleep(2)
        browser.execute_script('window.scrollTo(0,5*document.body.scrollHeight/8)')
        time.sleep(3)
        browser.execute_script('window.scrollTo(0,6*document.body.scrollHeight/8)')
        time.sleep(3)
        browser.execute_script('window.scrollTo(0,7*document.body.scrollHeight/8)')
        time.sleep(3)
        # browser.execute_script('window.scrollTo(0,8*document.body.scrollHeight/8)')
        # time.sleep(3)
        time.sleep(5)

    except TimeoutException:

        print('超时')
        index_page(nums)
    finally:
        page_source = browser.page_source
        return page_source


def parse_page(page_source):

    etree_html = etree.HTML(page_source)
    names = etree_html.xpath('//*[@class="good-info"]//div[3]/a/@title')
    prices = etree_html.xpath('/html/body/div[4]/div/div[3]/div[4]/div/div[3]/p[2]/span[@class="sale-price prime-cost"]/text()')
    image = etree_html.xpath('//div[contains(@class,"goods-container")]//a/img/@data-original')
    # print(image)
    for img in image:
        imgs ='http:' + img
        write_img(imgs)
    li = []
    for i in range(len(names)):
        dic = {}
        dic['name']=names[i]
        dic['price']=prices[i].strip()
        li.append(dic)
    with open('./shop.json', 'w', encoding='utf-8') as f:
        json.dump(li, f, ensure_ascii=False)


def write_img(imgs):
    global num
    imgs = requests.get(imgs)
    filename = './img/'+str(num)+'.jpg'
    with open(filename, 'wb')as f:
        f.write(imgs.content)
        print('下载%d张图片'% num)
        num += 1




def main():

    for nums in range(1, 1166):
        page_source = index_page(nums)
        parse_page(page_source)
        print(nums)

if __name__ == '__main__':
    main()

