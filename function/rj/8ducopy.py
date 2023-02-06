import urllib.request

# 请求的URL
url = "http://httpbin.org/get"
# 模拟浏览器打开网页(get请求)
res = urllib.request.urlopen(url)
print(res.read().decode("utf-8"))