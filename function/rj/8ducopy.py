# coding=utf-8
import re
import urllib.request, urllib.error
from bs4 import BeautifulSoup
import sys
import xlwt
import requests
sys.path.append("My-Actions/function/rj/")


baseurl = 'https://ruanjianku.cloud/'
def geturl(url):
    headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.70'
    }
    req = urllib.request.Request(url,headers=headers)
    html=""
    try:
        # urlopen()方法的参数，发送给服务器并接收响应
        resp = urllib.request.urlopen(req)
        # urlopen()获取页面内容，返回的数据格式为bytes类型，需要decode()解码，转换成str类型
        html = resp.read().decode('utf-8')
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
        return html

name=re.compile(r'lf"></span>(?P<name>.*?)</a>')
dizi=re.compile(r'<a href="(?P<dizi>.*?)".*?')
mos=re.compile(r'<p cp-post-excerpt>\n(?P<mos>.*?)</p>.*?</div>')
fenqu = re.compile(r'<a href=".*?cp-post-cat>(?P<fenqu>.*?)</a>')

# 定义接收10页的列表
dataList = []

def analysisData(baseurl):
    # item 是 bs4.element.Tag 对象，这里将其转换成字符串来处理
    item = str(item)
    # 定义一个列表 来存储每一个电影解析的内容
    data = []
    # findall返回的是一个列表，这里提取链接
    link = re.findall(findLink, item)[0]
    data.append(link)  # 添加链接
    img = re.findall(findImgSrc, item)[0]
    data.append(img)  # 添加图片链接
    title = re.findall(findTitle, item)
    # 一般都有一个中文名 一个外文名
    if len(title) == 2:
        # ['肖申克的救赎', '\xa0/\xa0The Shawshank Redemption']
        titlename = title[0] + title[1].replace(u'\xa0', '')
    else:
        titlename = title[0] + ""
        data.append(titlename)  # 添加标题
        pf = re.findall(findRating, item)[0]
        data.append(pf)
        pjrs = re.findall(findJudge, item)[0]
        data.append(pjrs)
        inqInfo = re.findall(inq, item)
        if len(inqInfo) == 0:
            data.append(" ")
        else:
            data.append(inqInfo[0])
        bd = re.findall(findBd, item)[0]
        # [('\n                            导演: 弗兰克·德拉邦特 Frank Darabont\xa0\xa0\xa0主演: 蒂姆·罗宾斯 Tim Robbins /...<br/>\n                            1994\xa0/\xa0美国\xa0/\xa0犯罪 剧情\n                        ', '\n\n                        \n                        ')]
        bd[0].replace(u'\xa0', '').replace('<br/>', '')
        bd = re.sub('<\\s*b\\s*r\\s*/\\s*>', "", bd[0])
        bd = re.sub('(\\s+)?', '', bd)
        data.append(bd)
        dataList.append(data)
    return dataList
        

# response = requests.request("GET", url, headers=headers)
# page_content = response.text
# obj = re.compile(r'<a href=".*?cp-post-cat>(?P<fenqu>.*?)</a>.*?'
#                  r'<a href="(?P<dizi>.*?)".*?'
#                  r'lf"></span>(?P<name>.*?)</a>.*?'
#                  r'<p cp-post-excerpt>\n(?P<mos>.*?)</p>.*?</div>', re.S)
# result = obj.finditer(page_content)
# for it in result:
#     fenqu=it.group("fenqu")
#     dizi=it.group("dizi")
#     name=it.group("name")
#     描述=it.group("mos")
#     print("分区：%s\t地址：%s\t软件：%s\n描述：%s" % (fenqu,dizi,name,描述))


def main():
    savepath = "function\\rj.xls"

    book = xlwt.Workbook(encoding="utf-8", style_compression=0)  # 创建Workbook对象
    sheet = book.add_sheet("软件", cell_overwrite_ok=True)  # 创建工作表
    col=("分区", "软件链接","软件","描述")
    print(len(dataList))
    print(len(dataList))
    for i in range(0, 4):
        sheet.write(0, i, col[i])
    for i in range(0, 0):
        print('正在保存第'+str((i+1))+'条')
        data = dataList[i]
        for j in range(len(data)):
            sheet.write(i + 1, j, data[j])
    book.save(savepath)
    

if __name__ == "__main__":
    main()