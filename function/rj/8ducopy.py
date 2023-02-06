import urllib.request
url = "https://ruanjianku.cloud/"
# 自定义headers
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
}
req = urllib.request.Request(url, headers=headers)
rw= urllib.request.urlopen(req).read().decode('utf-8')

import urllib.request,urllib.error

try:
    url = "https://ruanjianku.cloud/"
    req = urllib.request.Request(url, headers=headers)
    resp = urllib.request.urlopen(req)
    print(resp.read().decode('utf-8'))
# except urllib.error.HTTPError as e:
#     print("请检查url是否正确")
# URLError是urllib.request异常的超类
except urllib.error.URLError as e:
    if hasattr(e, "code"):
        print(e.code)
    if hasattr(e, "reason"):
        print(e.reason)