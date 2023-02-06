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
#                  r'<p cp-post-excerpt>\n(?P<mos>.*?)</p>.*?</div>', re.S)

# result = obj.finditer(page_content)

# print(result)

# if result:
#     for it in result:
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
        
# with open('./function/rj/rj.csv','r',newline='',encoding='utf-8') as f:
#     lst = list(set(f))
#     print(lst)
#     with open('./function/rj/rj1.csv','a+',newline='',encoding='utf-8') as f:
#         writer=csv.writer(f)
#         writer.writerow(f)

import pandas as pd

data = pd.read_excel("./function/rj/rj.csv")
#删除单位列的，空行数据
data.dropna(subset=['名字'], inplace=True)

# 第三步：获取 单位 列表并去重
department_list = list(data['名字'].drop_duplicates())  # 获取数据 单位 列，去重并放入列表
print(department_list)

# 第四步：按照类别分文件存放数据
for i in department_list:
    department = data[data['名字'] == i]
    department.to_excel('./' + str(i) + '名字.xlsx')