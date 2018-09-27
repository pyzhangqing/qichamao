import time
from lxml import etree
from selenium.common.exceptions import TimeoutException

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote


# 打开浏览器
browser = webdriver.Chrome()
# 设置浏览器大小
browser.set_window_size(1200, 700)
# 设置超时时间
wait = WebDriverWait(browser,20)
KEYWORD = '编程机器人'



def index_page(page):

    print(page)
    try:
        if page == 1:
            print('这是第一次')
            url='https://s.taobao.com/search?q=' + quote(KEYWORD)+'&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180914&ie=utf8'
            browser.get(url)
            browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            time.sleep(2)
            page_source = browser.page_source

        else:
            con = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.input.J_Input')))
            con.clear()
            con.send_keys(page)
            time.sleep(2)
            submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager div.form > span.btn.J_Submit')))
            submit.click()
            time.sleep(5)

    except TimeoutException:

        print('超时')
        index_page(page)
    page_source = browser.page_source

    return page_source


def parse_page(page_source):

    etree_html = etree.HTML(page_source)
    products = etree_html.xpath('//div[@id="mainsrp-itemlist"]//div[@class="items"]//div[contains(@class, "item")]')
    for product in products:
        item = {}
        item['price'] = product.xpath('.//div[contains(@class, "price")]/strong/text()')[0]
        item['shop'] = product.xpath('.//div[contains(@class, "shop")]/a/span[2]/text()')[0]
        item['image'] = product.xpath('.//div[@class="pic"]//img[contains(@class, "img")]/@data-src')[0].strip()
        item['deal'] = product.xpath('.//div[contains(@class, "deal-cnt")]//text()')[0]
        item['location'] = product.xpath('.//div[contains(@class, "location")]//text()')[0]
        print(item)




def main():

    for page in range(100):

        page_source = index_page(page+1)
        parse_page(page_source)

if __name__ == '__main__':
    main()

