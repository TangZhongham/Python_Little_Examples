"""
selenium获取news
"""
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


class Crawler(object):
    def __init__(self):
        self.site = 'https://www.anyknew.com/'
        self.headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0'}

    def get_code(self):
        try:
            result = requests.get(self.site)
        except Exception as e:
            print(e)
        else:
            return result.status_code

    def get_html(self):
        try:
            result = requests.get(self.site)
        except Exception as e:
            print(e)
        else:
            return result.content

    def get_session(self):
        try:
            driver = webdriver.Chrome("./driver/chromedriver")
            driver.maximize_window()
            driver.get(self.site)

            def re_do(driver):
                num = driver.find_element_by_xpath("//button[@class='op-btn']")
                num.click()
                WebDriverWait(driver, 1)
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
                WebDriverWait(driver, 1)
            for i in range(4):
                re_do(driver)

            print(driver.page_source)
        except Exception as e:
            print(e)
        else:
            return driver


if __name__ == '__main__':
    a = Crawler()
    b = a.get_session()
    b.find_element_by_class_name()