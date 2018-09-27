import time
from io import BytesIO

from PIL import Image
from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC
from lxml import etree
import requests

from chaojiying import main

browser = webdriver.Chrome()
url = 'http://www.chaojiying.com/user/login/'
wait = WebDriverWait(browser, 20)
browser.get(url)


user = 'pppigrui'
pd = 'XR19951105'


'''截屏获取验证码'''


def get_img():
    img = wait.until(EC.presence_of_element_located((By.XPATH, '//form//img')))#验证码
    time.sleep(2)
    location = img.location
    size = img.size
    top, bottom, left, right = location['y'], location['y'] + size['height'], location['x'], location['x'] + size[
        'width']

    screenshot = browser.get_screenshot_as_png()
    screenshot = Image.open(BytesIO(screenshot))
    captcha = screenshot.crop((left, top, right, bottom))#将截屏裁剪

    return captcha


def login_page():
    img = get_img()  # 获取到img对象
    img.save('code.png')  # 存为图片
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body > div.wrapper_danye > div > div.content_login')))
    username = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@name="user"]')))
    passwd = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@name="pass"]')))
    secret_code = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@name="imgtxt"]')))
    submit = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@class="login_form_input_submit"]')))
    time.sleep(3)
    username.send_keys(user)
    time.sleep(3)
    passwd.send_keys(pd)

    code = main()#调用超级鹰的main()函数 得到返回的验证码
    time.sleep(3)
    secret_code.send_keys(code)
    time.sleep(3)
    submit.click()


if __name__ == '__main__':
    login_page()
