"""
Don't Evil
"""
from selenium import webdriver
import time


class Crawler(object):
    def __init__(self):
        self.site = 'https://licai.p2peye.com/rebate/'
        self.headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0'}

    def get_site_list(self):
        site = self.site
        driver = webdriver.Chrome()
        try:
            driver.get(site)
            target_list = driver.find_elements_by_css_selector('[title=查看详情]')
            if target_list:
                print("Success")
                url_list = []
                for i in target_list:
                    url = i.get_attribute('href')
                    url_list.append(url)
                return url_list
        finally:
            print(1)
            driver.close()

    def auto_click(self, site, NUM):
        driver = webdriver.Chrome()
        try:
            driver.get(site)
            button = driver.find_element_by_css_selector("[api-event=login")
            try:
                button.click()
                phone_num = driver.find_element_by_css_selector("[name=mobile]")
                if phone_num:
                    phone_num.send_keys(NUM)
                    auth_code = driver.find_element_by_css_selector("[id=getCode]")
                    if auth_code:
                        auth_code.click()
                        print('验证码获取完毕')
                        close_btn = driver.find_element_by_css_selector("[class=signload-close-btn]")
                        if close_btn:
                            close_btn.click()
                    else:
                        print('验证码获取失败')
                else:
                    print('未达到输入界面')
            except Exception as e:
                print('未找到点击按钮')
            finally:
                pass
            return 1
        except Exception as e:
            return e
        finally:
            print('成功注册一个页面')


if __name__ == "__main__":
    while True:
        NUM = '18998997909'
        a = Crawler()
        url_list = a.get_site_list()
        print(url_list)
        # url = 'https://licai.p2peye.com/rebate/4289-1-2.html'
        for url in url_list:
            a.auto_click(url, NUM)
        print('已注册{}个网站'.format(len(url_list)))
        time.sleep(300)
