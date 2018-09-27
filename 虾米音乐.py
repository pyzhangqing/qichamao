import requests
from lxml import etree
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from kaisha import str2url


browser = webdriver.Chrome()
browser.set_window_size(1000,500)
wait = WebDriverWait(browser,10)


def index_page():
    try:
        url = 'https://www.xiami.com/chart?spm=a1z1s.6843761.1110925385.2.wOEHD4'
        browser.get(url)
        value = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#body #chart .songwrapper')))

    except TimeoutException:
        index_page()

    page_source = browser.page_source

    return page_source


def prase_page(page_source):
    etree_html = etree.HTML(page_source)
    content = etree_html.xpath('//div[@id="chart"]/table/tr')
    print(content)

    for i in content:
        item = {}
        item['data'] = i.xpath('./@data-mp3')[0]
        item['title'] = i.xpath('./@data-title')[0].replace('?', 'u')

        mp3_link = item['data']
        mp3_url = str2url(mp3_link)
        r = requests.get(mp3_url)
        print(item['title'])
        filename = './media/%s.mp3' % item['title']
        with open(filename, 'wb') as f:
            f.write(r.content)

#

def main():


    page_source = index_page()

    prase_page(page_source)


if __name__ == '__main__':
    main()
