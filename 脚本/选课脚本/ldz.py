import requests

url = "http://xsxk.nuist.edu.cn/xsxk/elective/clazz/add"
headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Authorization": "eyJhbGciOiJIUzUxMiJ9.eyJ0aW1lIjoxNzM1OTE0NjcwMjA5LCJsb2dpbl91c2VyX2tleSI6IjIwMjI4MzI5MDE1OSIsInRva2VuIjoiNmNqZTMwMTNmY2lvZ291MjJlaTkza3JhbGEifQ.SAROuodz8NCK0_a4pgsdUMnzo-TGem960V5bokeF4rBGccZebDEI1_qLIQgNfAwgCgoHVM-nd5G3nZ2SFKyHTg",
    "Content-Length": "232",
    "Content-Type": "application/x-www-form-urlencoded",
    "Cookie": "route=9b588388c72efc64461890c4edb3d800; Authorization=eyJhbGciOiJIUzUxMiJ9.eyJ0aW1lIjoxNzM1OTE0NjcwMjA5LCJsb2dpbl91c2VyX2tleSI6IjIwMjI4MzI5MDE1OSIsInRva2VuIjoiNmNqZTMwMTNmY2lvZ291MjJlaTkza3JhbGEifQ.SAROuodz8NCK0_a4pgsdUMnzo-TGem960V5bokeF4rBGccZebDEI1_qLIQgNfAwgCgoHVM-nd5G3nZ2SFKyHTg",
    "Host": "xsxk.nuist.edu.cn",
    "Origin": "http://xsxk.nuist.edu.cn",
    "Proxy-Connection": "keep-alive",
    "Referer": "http://xsxk.nuist.edu.cn/xsxk/elective/grablessons?batchId=c8bb0a897f4e40e2a4b65ffd5c61124b",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0"
}

data = {
    "batchid": "c8bb0a897f4e40e2a4b65ffd5c61124b"
}
data.update({
    "clazzType": "FANKC",
    "clazzId": "2024202521500009234",
    "secretVal": "jzzDBZTsoWK1ySB54j7sBqWQkhiBmfXmZFX2waqIYXsVtYv/C4GCVAMRHP4p6JY7TUtJi1Yo0EcTaYgo18L8gaArzwqIVVl8mGitgMKcx+Yi2czSLOFubHzBI01VGaBHvTPO3L9MTm2gNkYhrrL3rQ7cVV4SKxofYhbPxxdeNtg="
})
response = requests.post(url, headers=headers, data=data)

print(response.status_code)
print(response.json())
import time

while True:
    time.sleep(0.5)
    response = requests.post(url, headers=headers, data=data)
    print(response.status_code)
    print(response.json())