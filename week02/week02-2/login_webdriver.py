from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    # 需要安装chrome driver, 和浏览器版本保持一致
    # http://chromedriver.storage.googleapis.com/index.html
    
    browser.get('https://shimo.im/login?from=home')
    time.sleep(1)

    browser.find_element_by_xpath('//input[@name="mobileOrEmail"]').send_keys('test')
    browser.find_element_by_xpath('//input[@name="password"]').send_keys('test')
    browser.find_element_by_xpath('//button[text()="立即登录"]').click()

except Exception as e:
    print(e)
finally:    
    browser.close()
    