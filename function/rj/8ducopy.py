# coding=utf-8
import re
import sys
import csv
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
#                  r'<p cp-post-excerpt>\n(?P<mos>.*?)</p>.*?</div>.*?'
#                  r'<span>(?P<riqi>.*?)</span>', re.S)

# result = obj.finditer(page_content)

# if result:
#     for it in result:
#         with open('./function/rj/rj1.csv','a',newline='',encoding='utf-8') as f:
#             writer=csv.writer(f)
#             fenqu=it.group("fenqu")
#             riqi=it.group("riqi")
#             dizi= it.group("dizi")
#             name= it.group("name")
#             mos = it.group("mos")
#             L=[fenqu,riqi,dizi,name,mos]
#             writer.writerow(L)
#             print(fenqu,riqi,dizi,name,mos)