# coding=utf-8
import re
import sys
import csv
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

result = obj.finditer(page_content)

# print(result)

if result:
    for it in result:
        # print("分区：",it.group("fenqu"))
        # print("地址：",it.group("dizi"))
        # print("软件：",it.group("name"))
        # print("描述：",it.group("mos"))
        # print(20*'*')
        # with open('./function/rj/rj.csv','a',newline='',encoding='utf-8') as f:
        #     writer=csv.writer(f)
        #     fenqu=it.group("fenqu")
        #     dizi= it.group("dizi")
        #     name= it.group("name")
        #     mos = it.group("mos")
        #     L=[fenqu,dizi,name,mos]
        #     writer.writerow(L)
        #     # print(fenqu,dizi,name,mos)
        
        with open('./function/rj/rj.csv') as f:
            lst = list(set(f))
            print(lst)