"""
20190805
for 笕美和子/Miwako Kakei
"""
import os

import requests
from bs4 import BeautifulSoup


URL = 'https://www.meituri.com/t/2067/'


class MKer:
    def __init__(self):
        self.url = URL

    def get_list(self):
        """"获取所有相册列表"""
        html = requests.get(self.url)
        target_list = {}
        if html.status_code != 200:
            print("网站登陆失败")
            return 0
        content = html.content
        soup = BeautifulSoup(content, "html.parser")
        print("正在爬取 {} ...".format(soup.title.name))
        section = soup.find("div", class_="hezi").find_all("li")
        for i in section:
            target_url = i.find("a")["href"]
            name = i.find("p", class_="biaoti").string[-50:]
            target_list[name] = target_url
            print("\n找到" + name + target_url)
        print("共有 {} 个专辑".format(len(target_list)))
        return target_list

    def download_img(self, target_list):
        def scrap_img(url, file_path):
            html = requests.get(url)
            if html.status_code != 200:
                pass
            content = html.content
            soup = BeautifulSoup(content, 'html.parser')
            image_bar = soup.find("div", class_="content")
            image_list = image_bar.find_all("img")
            for each_img in image_list:
                img_url = each_img["src"]
                img_name = each_img["alt"].replace('/', '／').replace('\\', '＼')
                down_load = requests.get(img_url).content
                with open(file_path + '/' + img_name + '.jpg', 'wb') as f:
                    f.write(down_load)
                print("\n {} 下载成功".format(img_name))
            return 1

        if not os.path.exists("photo"):
            os.mkdir("photo")
        for name, url in target_list.items():
            name = name.replace('/', '／') .replace('\\', '＼')
            file_path = "photo/" + name
            if not os.path.exists(file_path):
                os.mkdir(file_path)
            html = requests.get(url)
            if html.status_code != 200:
                pass
            content = html.content
            soup = BeautifulSoup(content, 'html.parser')
            all_pages = soup.find("div", id="pages").find_all("a")[-2].string
            print(all_pages)

            image_bar = soup.find("div", class_="content")
            image_list = image_bar.find_all("img")
            for each_img in image_list:
                img_url = each_img["src"]
                img_name = each_img["alt"].replace('/', '／').replace('\\', '＼')
                down_load = requests.get(img_url).content
                with open(file_path + '/' + img_name + '.jpg', 'wb') as f:
                    f.write(down_load)
                print("\n {} 下载成功".format(img_name))

            for i in range(2, int(all_pages)+1):
                next_url = url + str(i) + '.html'
                x = scrap_img(next_url, file_path)
                if x == 1:
                    print("Success")


if __name__ == '__main__':
    target_list = MKer().get_list()
    print(target_list)
    MKer().download_img(target_list)



