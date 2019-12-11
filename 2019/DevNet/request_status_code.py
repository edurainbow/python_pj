#__author:"Peter"
#date:2019/12/4
import requests
r = requests.get('http://127.0.0.1:6868')
print(r.ok)
#状态码
print(r.status_code)
#如果发送了一个错误请求（一个4xx客户端错误，或者5XX服务器错误响应），我们可以通过Response.raise_for_status()来抛出异常
#由于访问http://127.0.0.1:6868的状态码为200，所以不会产生异常
r.raise_for_status()

r = requests.get('http://127.0.0.1:6868/dfdfd')

print(r.ok)
#状态码
print(r.status_code)
#如果发送了一个错误请求（一个4xx客户端错误，或者5XX服务器错误响应），我们可以通过Response.raise_for_status()来抛出异常
r.raise_for_status()