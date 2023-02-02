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

obj = re.compile(r'<a href=".*?"target=".*?"cppost-cat=".*?"class="link-instanted">(?P<fenqu>.*?)</a>' )
result = obj.finditer(page_content)
for it in result:
    fqu=it.group('fenqu')
    print(it.group("fenqu"))
    # print(it.group("id"))
    # print(it.group("wahaha"))

# print(response.text)
