# coding=utf-8
import re
import sys
import requests
sys.path.append("My-Actions/function/rj/")
# from sendNotify import *

url='https://ruanjianku.cloud/'
headers = {
    'content-type': 'text/html; charset=UTF-8',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.70'
}
# def comic(comic):
#     print(comic)

response = requests.request("GET", url, headers=headers)
page_content = response.text

# obj = re.compile(r'<a href=".*" target=".*" cp-post-cat>(?P<fenqu>.*?)</a>',re.S)
obj=re.compile(r'<a href="(?P<dizi>.*?)" target="_self"></span>(?P<name>.*?)</a>\n</h2>\n<p cp-post-excerpt>\n(?P<mos>.*?)\n</p>')
# obj = re.compile(r'<a href="(?P<dizi>.*?)" target="_self"></span>(?P<name>.*?)</a>'
#                 #  r'<a href=".*" target=".*" cp-post-cat>(?P<fenqu>.*?)</a>'
#                  r'<p cp-post-excerpt>\n(?P<mos>.*?)\n</p>')

result = obj.finditer(page_content)
for it in result:
    diz=it.group("dizi")
    # 分区=it.group("fenqu")
    name=it.group("name")
    描述=it.group("mos")
    print("地址：%s\t分区：%s\t软件名：%s\t描述：%s" % (diz, 分区, name, 描述))
    # fqu=it.group('fenqu')
    # print(it.group("fenqu").strip())

    # print(it.group("dizi"))

    print("完成!")

# print(response.text)
