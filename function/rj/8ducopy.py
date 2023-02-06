# coding=utf-8
import re
import time
import sys
from urllib import request
import csv
import random
import requests
sys.path.append("My-Actions/function/rj/")

url='https://ruanjianku.cloud/'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.70'
}

response = requests.request("GET", url, headers=headers)
page_content = response.text

obj = re.compile(r'<a href=".*?cp-post-cat>(?P<fenqu>.*?)</a>.*?'
                 r'<a href="(?P<dizi>.*?)".*?'
                 r'lf"></span>(?P<name>.*?)</a>.*?'
                 r'<p cp-post-excerpt>\n(?P<mos>.*?)</p>.*?</div>', re.S)

result = obj.findall(page_content)

print(result)

if result:
    for result in result:
        print("分区：",result[0])
        print("地址：",result[1])
        print("软件：",result[2])
        print("描述：",result[3].strip())
        print(20*'*')
    with open('function\\rj\\rj.csv','a',newline='',encoding='utf-8') as f:
            writer=csv.writer(f)
            for r in result:
                fenqu=result[0].strip()
                dizi=result[1].strip()
                name=result[2].strip()
                mos=result[3].strip()[5:]
                L=[fenqu,dizi,name,mos]
                writer.writerow(L)
                print(fenqu,dizi,name,mos)