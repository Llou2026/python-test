"""
    在一般的使用上，requests和urllib没有太大区别，但是在复杂的场景中，requests可以提供urllib无法提供的强大功能。
    因此，在使用上，建议使用requests库代替urllib库来进行HTTP请求等的操作。
"""
import requests
response = requests.get('https://www.baidu.com')
content = str(response.content,encoding='utf-8')
content_list = content.split('\n')#分行
l=len(content_list)#打印页面内容的行数
print(l)
#print(content)
for line in content_list:
    if 'href' in line and 'www' in line:
        #line.lstrip() 只清洗左边
        #line.rsplit() 只清洗右边
        print(line.strip())