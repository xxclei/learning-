import requests

import base64
from urllib.parse import urlsplit

payload = {
    "teachingClassType": "FANKC",
    "pageNumber": 1,
    "pageSize": 10,
    "orderBy": "",
    "campus": "1",
    "SFYX": "2"
}
# print(data)
import pandas as pd
# URL of the login endpoint
url = "http://xsxk.nuist.edu.cn/xsxk/auth/login"
url_s = "http://xsxk.nuist.edu.cn/xsxk/elective/clazz/list"












def get_captcha():
    captcha_url = "http://xsxk.nuist.edu.cn/xsxk/auth/captcha"
    captcha_headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Content-Type": "application/json;charset=UTF-8",
        "Origin": "http://xsxk.nuist.edu.cn",
        "Referer": "http://xsxk.nuist.edu.cn/xsxk/profile/index.html",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0",
        "Cookie": "Authorization=eyJhbGciOiJIUzUxMiJ9.eyJ0aW1lIjoxNzM1OTE0NjcwMjA5LCJsb2dpbl91c2VyX2tleSI6IjIwMjI4MzI5MDE1OSIsInRva2VuIjoiNmNqZTMwMTNmY2lvZ291MjJlaTkza3JhbGEifQ.SAROuodz8NCK0_a4pgsdUMnzo-TGem960V5bokeF4rBGccZebDEI1_qLIQgNfAwgCgoHVM-nd5G3nZ2SFKyHTg; route=33efcd2f3cc6ef258b1dbadfba047ee9"
    }
    
    response = requests.post(captcha_url, headers=captcha_headers).json()
    captcha_data = response['data']['captcha']
    uuid=response['data']['uuid']
    # Decode the base64 image data
    header, encoded = captcha_data.split(",", 1)
    data = base64.b64decode(encoded)
    
    # Send the image to the API for recognition
    api_url = "https://imgcode.toolshu.com/api"
    api_token = "ts_0VLAG7EEMK5EILKXBDLSIRNFR"  # Replace with your actual token
    files = {
        "token": api_token,
        "file": captcha_data
    }
    response = requests.post(api_url, json=files)
    cp = response.json().get('data')
    print(cp)
    return cp,uuid




    response = session.post(url, headers=headers, json=payload)
    data=response.json().get('data').get('rows')[0].get('tcList')
    limit=[cl.get('limitKindList') for cl in data]

# print(data)


    c=[c for c in data ]
    teacher=[cl.get('SKJS') for cl in c]
    secretVal=[cl.get('secretVal') for cl in c]
    classI=[cl[0] for cl in limit]
    print(classI)
    classId=[cl[0].get('teachingClassID') for cl in limit]


    print(classId)
    dict1 = dict(zip(teacher, secretVal))
    dict2 = dict(zip(teacher, classId))
    df = pd.DataFrame(list(dict1.items()), columns=['teacher', 'secretVal'])
    df['classId'] = df['teacher'].map(dict2)

    df.to_csv('output.csv', index=False, encoding='utf-8-sig')






# Headers for the request
headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "http://xsxk.nuist.edu.cn",
    "Referer": "http://xsxk.nuist.edu.cn/xsxk/profile/index.html",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0",
   
}
captha,uuid=get_captcha()
# Data for the POST request
data = {
    # Add the required form data here
    "loginname": "202283290159",
    "password": "N6PH9JqTFm/YzBXEON9/XA==",
    'captcha': captha,
    'uuid': uuid
}

# 创建一个会话
session = requests.Session()
# 使用会话执行POST请求
response = session.post(url, data=data)


if response.status_code == 200:
    print("登录成功")

    # 更新标头
    session.headers.update({
        "Authorization": response.json().get("data").get("token"),
        "Cookie": f"route=33efcd2f3cc6ef258b1dbadfba047ee9; Authorization={response.json().get('data').get('token')}"
    })

    



data2={'batchId': 'c8bb0a897f4e40e2a4b65ffd5c61124b'}
response2 = session.post('http://xsxk.nuist.edu.cn/xsxk/elective/user', data=data2)

print(response.status_code)
print(response.json())
print(response2.json())





def get_secret_data(url_s, session, payload):
    response = session.post(url_s,  json=payload)
    data=response.json().get('data').get('rows')[0].get('tcList')
    limit=[cl.get('limitKindList') for cl in data]
    c=[c for c in data ]
    teacher=[cl.get('SKJS') for cl in c]
    secretVal=[cl.get('secretVal') for cl in c]
    classI=[cl[0] for cl in limit]
    classId=[cl[0].get('teachingClassID') for cl in limit]

    dict1 = dict(zip(teacher, secretVal))
    dict2 = dict(zip(teacher, classId))
    df=pd.DataFrame(list(dict1.items()),columns=['teacher','secretVal'])
    df2=pd.DataFrame(list(dict2.items()),columns=['teacher','classId'])

    print(df['teacher'])
    teacher_id=input("请输入教师序号：")
    target_secretVal=df.loc[int(teacher_id),'secretVal']
    target_classId=df2.loc[int(teacher_id),'classId']
    print(target_classId)
    print(target_secretVal)

    return target_classId,target_secretVal

target_classId,target_secretVal=get_secret_data(url_s, session, payload)

data = {
    "batchid": "c8bb0a897f4e40e2a4b65ffd5c61124b"
}
data.update({
    "clazzType": "FANKC",
    "clazzId": target_classId,
    "secretVal": target_secretVal
})
import time

while(True):
    time.sleep(0.5)
    response = session.post("http://xsxk.nuist.edu.cn/xsxk/elective/clazz/add", data=data)
# 打印响应状态码和响应内容

    print(response.status_code)
    print(response.json())

