# coding=utf-8
import re
import sys
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
for it in result:
    fenqu=it.group("fenqu")
    dizi=it.group("dizi")
    name=it.group("name")
    描述=it.group("mos")
    print("分区：%s\t地址：%s\t软件：%s\n描述：%s" % (fenqu,dizi,name,描述))

