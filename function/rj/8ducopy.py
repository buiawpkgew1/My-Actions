# coding=utf-8
import re
import time
import sys
from urllib import request
import csv
import random
import requests
sys.path.append("My-Actions/function/rj/")

# url='https://ruanjianku.cloud/'
# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.70'
# }

# response = requests.request("GET", url, headers=headers)
# page_content = response.text

# obj = re.compile(r'<a href=".*?cp-post-cat>(?P<fenqu>.*?)</a>.*?'
#                  r'<a href="(?P<dizi>.*?)".*?'
#                  r'lf"></span>(?P<name>.*?)</a>.*?'
#                  r'<p cp-post-excerpt>\n(?P<mos>.*?)</p>.*?</div>', re.S)

# result = obj.findall(page_content)

# print(result)

# if result:
#     for result in result:
#         print("分区：",result[0])
#         print("地址：",result[1])
#         print("软件：",result[2])
#         print("描述：",result[3].strip())
#         print(20*'*')
class MaoyanSpider(object): 
    def __init__(self):
        self.url = 'https://ruanjianku.cloud/'

    def get_html(self,url):
        headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.70'}
        req= requests.Request(url=url,headers=headers)
        res=requests.URLRequired(req)
        html= res.read().decode()
        # 直接调用解析函数
        self.parse_html(html)
    def parse_html(self,html):
        re_bds=r'<a href=".*?cp-post-cat>(?P<fenqu>.*?)</a>.*?<a href="(?P<dizi>.*?)".*?lf"></span>(?P<name>.*?)</a>.*?<p cp-post-excerpt>\n(?P<mos>.*?)</p>.*?</div>'
        # 生成正则表达式对象
        pattern= re.compile(re_bds,re.S)
        r_list=pattern.findall(html)
        self.save_html(r.list)
    def save_html(self,r_list):
        with open('function\\rj\\rj.csv','a',newline='',encoding='utf-8') as f:
            writer=csv.writer(f)
            for r in r_list:
                fenqu=r[0].strip()
                dizi=r[1].strip()
                name=r[2].strip()
                mos=r[3].strip()[5:]
                L=[fenqu,dizi,name,mos]
                writer.writerow(L)
                print(fenqu,dizi,name,mos)
    def run(self):
        for offset in 2:
            self.get_html(url)
            time.sleep(random.uniform(1,2))
if __name__=='__name__':
    try:
        spider=MaoyanSpider()
        spider.run()
    except Exception as e:
        print('错误:',e)