#__author:"Peter"
#date:2019/12/4
import requests
#由于数字证书有效，所以直接可以得到结果
r = requests.get('https://www.jd.com')
print(r.text)

#下面两句用于禁止告警信息
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#192.168.1.4为路由器自签名证书，所以需要verify=False
# r=requests.get('https://127.0.0.1/webui/',verify=False)
# print(r.text)