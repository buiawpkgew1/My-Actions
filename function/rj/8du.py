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
data_set = set()
for obj in re.finditer(r'<a href=".*?cp-post-cat>(?P<fenqu>.*?)</a>.*?'
                 r'<a href="(?P<dizi>.*?)".*?'
                 r'lf"></span>(?P<name>.*?)</a>.*?'
                 r'<p cp-post-excerpt>\n(?P<mos>.*?)</p>.*?</div>.*?'
                 r'<span>(?P<riqi>.*?)</span>', page_content, re.S):
        fenqu=obj.group("fenqu")
        dizi= obj.group("dizi")
        name= obj.group("name")
        mos = obj.group("mos")
        riqi= obj.group("riqi")
        data_set.add((fenqu,riqi,dizi,name,mos))
with open('./function/rj/rj.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(headers) 
    writer.writerows(list(data_set))