import urllib.request
url = "https://ruanjianku.cloud/"
res = urllib.request.urlopen(url)  # get方式请求
print(res)  # 返回HTTPResponse对象<http.client.HTTPResponse object at 0x00000000026D3D00>


# # 读取响应体
# bys = res.read()  # 调用read()方法得到的是bytes对象。
# # print(bys)  # <!DOCTYPE html><!--STATUS OK-->\n\n\n    <html><head><meta...
# print(bys.decode("utf-8"))  # 获取字符串内容，需要指定解码方式,这部分我们放到html文件中就是百度的主页
 
# # 获取HTTP协议版本号(10 是 HTTP/1.0, 11 是 HTTP/1.1)
# print(res.version)  # 11
 
# # 获取响应码
# print(res.getcode())  # 200
# print(res.status)  # 200
 
# # 获取响应描述字符串
# print(res.reason)  # OK
 
# # 获取实际请求的页面url(防止重定向用)
# print(res.geturl())  # http://www.baidu.com/
 
# # 获取响应头信息,返回字符串
# print(res.info())  # Bdpagetype: 1 Bdqid: 0x803fb2b9000fdebb...
# # 获取响应头信息,返回二元元组列表
# print(res.getheaders())  # [('Bdpagetype', '1'), ('Bdqid', '0x803fb2b9000fdebb'),...]
# print(res.getheaders()[0])  # ('Bdpagetype', '1')
# # 获取特定响应头信息
# print(res.getheader(name="Content-Type"))  # text/html;charset=utf-8