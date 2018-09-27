from lxml import etree
from selenium.common.exceptions import TimeoutException

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote


# 打开浏览器
browser = webdriver.Chrome()
# 设置浏览器大小
browser.set_window_size(1200,700)
# 设置超时时间
wait = WebDriverWait(browser,10)
KEYWORD = '超人'

def index_page():
    try:
        url='https://movie.douban.com/subject_search?search_text='+ quote(KEYWORD)+'&cat=1002'
        browser.get(url)
        # browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        submit = wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, '下一页')))
        submit.click()

    except TimeoutException:

        index_page()
    page_source = browser.page_source
    return page_source


def parse_page(page_source):

    etree_html = etree.HTML(page_source)
    contents = etree_html.xpath('//div[@id="listContent"]//div[@class="itemBox descBox"]')

    for i in contents:
        item={}
        item['saray']=i.xpath('.//div[@class="jobDesc"]/p/text()')
        item['adress']=i.xpath('.//ul[@class="job_demand"]/li/text()')
        print(item)
        return item



def main():

        page_source = index_page()

        parse_page(page_source)



if __name__ == '__main__':
    main()

