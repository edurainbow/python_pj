#__author:"Peter"
#date:2019/12/4
import requests
request_result = requests.get('http://192.168.62.221:6868/rpc/datetime')
print(request_result.json())
request_result = requests.get('http://192.168.62.221:6868/rpc/date')
print(request_result.json())
request_result = requests.get('http://192.168.62.221:6868/rpc/other')
print(request_result.json())
