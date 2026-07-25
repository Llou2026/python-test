"""
from urllib import request
response = request.urlopen('https://www.imooc.com')#向慕课网发出请求
print(response.status)
for k, v in response.getheaders():
    print('{}: {}'.format(k, v))
"""
import requests
print(requests.__version__)

response = requests.get('https://www.imooc.com')
print(response.status_code)#打印转台码
print(response.headers)#打印回应头