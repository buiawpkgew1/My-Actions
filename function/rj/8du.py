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
# print(page_content)

# obj=re.compile(r'<a href=.*.cp-post-cat>(?P<fenqu>.*?)</a>\n.*\n.*\n.*\n.*\n.*\n<a href="(?P<dizi>.*?)".*an>(?P<name>.*?)</a>\n.*\n.*\n(?P<mos>.*?)\n')
# obj = re.compile(r'<a href=.*?cp-post-cat>(?P<fenqu>.*?)</a>\n.*\n.*\n.*\n.*\n.*\n'
#                  r'<a href="(?P<dizi>.*?)" target="_self"></span>(?P<name>.*?)</a>'
#                  r'<p cp-post-excerpt>\n(?P<mos>.*?)\n')
obj=re.compile(r'<a href=.*.cp-post-cat>(?P<fenqu>.*?)</a>.*<a href="(?P<dizi>.*?)".*an>(?P<name>.*?)</a>.*<p cp-post-excerpt>(?P<mos>.*?)</p>\n',re.S)

result = obj.finditer(page_content)
for it in result:
    fenqu=it.group("fenqu")
    dizi=it.group("dizi")
    name=it.group("name")
    描述=it.group("mos")
    print(it.group("fenqu"))
    print(it.group("dizi"))
    print(it.group("name"))
    print(it.group("mos"))
    # print("分区：%s\t软件名：%s\t描述：%s\t地址：%s" % (fenqu, name, 描述, dizi))
    # print("完成？")

# print(response.text)
