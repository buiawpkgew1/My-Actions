# coding=utf-8
import sys
import requests
sys.path.append("My-Actions/function/rj/")
from sendNotify import *

url='https://ruanjianku.cloud/'
headers = {
   'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.70'
}
response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)