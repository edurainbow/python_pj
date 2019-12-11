#__author:"Peter"
#date:2019/12/4
import requests
request_result = requests.post('http://127.0.0.1:6868/formtest',data={'name':'collinsctk','age':40})
print(request_result.text)
request_result = requests.post('http://127.0.0.1:6868/rpc_function',json={'function':'datetime'})
print(request_result.json())
request_result = requests.post('http://127.0.0.1:6868/rpc_function',json={'function':'date'})
print(request_result.json())
request_result = requests.post('http://127.0.0.1:6868/rpc_function',json={'function':'other'})
print(request_result.json())

