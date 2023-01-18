from urllib.request import urlopen

# decode格式

url = 'http://www.baidu.com'
resp = urlopen(url)
t = resp.read().decode('utf-8')
print(t)

with open("1.html",'w',encoding='utf-8') as f:
    f.write(t)
print("over!")

555