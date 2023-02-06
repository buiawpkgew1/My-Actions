import urllib.request
 
url = "https://ruanjianku.cloud/"
# 自定义headers
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
}
req = urllib.request.Request(url, headers=headers)
# urlopen(也可以是request对象)
print(urllib.request.urlopen(req).read().decode('utf-8'))