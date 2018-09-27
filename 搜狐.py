import requests
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
browser.set_window_size(1200,700)
# 设置超时时间
wait = WebDriverWait(browser,10)


def index_page():
    try:
        url='http://news.sohu.com/'
        browser.get(url)
        # browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        submit = wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, '登录狐友')))
        submit.click()

    except TimeoutException:

        index_page()
    page_source = browser.page_source
    # browser.close()
    return page_source


def parse_page(page_source):

    html = etree.HTML(page_source)
    img = html.xpath('//div[@class="login mobile-login"]/ul/li[@class="short"]/img/@src')[0]
    print(img)
    l = requests.get(img)
    filename='./image/1.jpg'
    with open(filename,'wb')as f:
        f.write(l.content)

    return l





def main():

        page_source = index_page()

        parse_page(page_source)



if __name__ == '__main__':
    main()

