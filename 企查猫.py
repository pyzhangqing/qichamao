
import time
from io import BytesIO
from selenium.common.exceptions import TimeoutException
from PIL import Image
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from chaojiying import main



browser = webdriver.Chrome()
browser.maximize_window()

wait = WebDriverWait(browser, 10)
user='18223583248'
password='panglove=520ht'



def get_image():
    img = wait.until(EC.presence_of_element_located((By.XPATH, '//img[@id="login_code_img"]')))  # 验证码
    time.sleep(2)
    location = img.location
    size = img.size
    top, bottom, left, right = location['y'], location['y'] + size['height'], location['x'], location['x'] + size[
        'width']
    screenshot = browser.get_screenshot_as_png()
    screenshot = Image.open(BytesIO(screenshot))
    captcha = screenshot.crop((left, top, right, bottom))

    return captcha


def index_page():
    try:
        url = 'https://www.qichamao.com/'
        browser.get(url)
        login = wait.until(EC.presence_of_element_located((By.ID, 'hdbar-login')))
        login.click()
        user_login = wait.until(EC.presence_of_element_located((By.XPATH, '//li[@id="md-form-login-password"]/a')))
        user_login.click()
        phone = wait.until(EC.presence_of_element_located((By.ID, 'form_phone')))
        passd = wait.until(EC.presence_of_element_located((By.ID, 'form_password')))
        phone.send_keys(user)
        passd.send_keys(password)

        imge = get_image()
        imge.save('code.png')
        check = wait.until(EC.presence_of_element_located((By.ID, 'form_verifycode')))

        code = main()
        print(code)
        time.sleep(2)
        check.send_keys(code)
        check.click()
        login = wait.until(EC.element_to_be_clickable((By.ID, 'form_userlogin')))
        login.click()

    except TimeoutException:
        print('超时')



if __name__ == '__main__':
    # # 保存图片
    # image_name = 'pic.png'
    index_page()







