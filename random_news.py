"""
随机获取20条新闻并且发送邮件
"""
import requests
import random


class RandomNews(object):
    """随机抽取20条新闻并（发送邮件）"""
    def __init__(self):
        self.base_url = 'https://www.anyknew.com/api/v1/cats/'
        self.cat_list = ['universal', 'st', 'life', 'ent']
        self.headers = {'User-Agent':
                        'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0'}

    def get_content(self):
        """爬取网站的raw_content"""
        target = self.cat_list
        content = []
        for item in target:
            url = self.base_url + item
            get_page = requests.get(url, headers=self.headers)
            if get_page.status_code == 200:
                raw_info = get_page.json()
                content.append(raw_info)
        return content

    def get_text(self, content=False):
        """处理json并返回所有news列表"""
        content = content if content is not False else self.get_content()
        news_list = []
        for item in content:
            content_list = item["data"]['cat']['sites']
            for i in content_list:
                text_list = i['subs']
                for each_text_list in text_list:
                    x = each_text_list['items']
                    for i in x:
                        one_text = i['title']
                        news_list.append(one_text)
        return news_list

    def get_random_news(self, news_list=False, n=20):
        """随机返回n条消息"""
        news_list = news_list if news_list is not False else self.get_text()
        news = '\n'.join(random.sample(news_list, n))
        return news


if __name__ == '__main__':
    a = RandomNews()
    x = a.get_random_news()
    print(x)
