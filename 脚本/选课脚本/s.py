import requests
import pandas as pd
url = "http://xsxk.nuist.edu.cn/xsxk/elective/clazz/list"
headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Authorization": "eyJhbGciOiJIUzUxMiJ9.eyJ0aW1lIjoxNzM1OTExODQyNzMyLCJsb2dpbl91c2VyX2tleSI6IjIwMjI4MzI5MDE1OSIsInRva2VuIjoicjliZ2duNTU1MmphMm8wM2tqY2w5NDRkNnQifQ.vfGD1qcI7mvPrHrjyUwF93lGJgLGcKX5xADVf3XYbD5BKDeE9MVtf8fKz-qnS9gzugPpVJevOxJS3qgQ5S-w4g",
    "Content-Type": "application/json;charset=UTF-8",
    "Cookie": "route=d8cecf068f7a4defeff6372ece59245d; Authorization=eyJhbGciOiJIUzUxMiJ9.eyJ0aW1lIjoxNzM1OTExODQyNzMyLCJsb2dpbl91c2VyX2tleSI6IjIwMjI4MzI5MDE1OSIsInRva2VuIjoicjliZ2duNTU1MmphMm8wM2tqY2w5NDRkNnQifQ.vfGD1qcI7mvPrHrjyUwF93lGJgLGcKX5xADVf3XYbD5BKDeE9MVtf8fKz-qnS9gzugPpVJevOxJS3qgQ5S-w4g",
    "Host": "xsxk.nuist.edu.cn",
    "Origin": "http://xsxk.nuist.edu.cn",
    "Proxy-Connection": "keep-alive",
    "Referer": "http://xsxk.nuist.edu.cn/xsxk/elective/grablessons?batchId=c8bb0a897f4e40e2a4b65ffd5c61124b",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0"
}


def get_secret(url, headers):
    payload = {
    "teachingClassType": "FANKC",
    "pageNumber": 1,
    "pageSize": 10,
    "orderBy": "",
    "campus": "1",
    "SFYX": "2"
}

    response = requests.post(url, headers=headers, json=payload)
    data=response.json().get('data').get('rows')[0].get('tcList')
    limit=[cl.get('limitKindList') for cl in data]

# print(data)


    c=[c for c in data ]
    teacher=[cl.get('SKJS') for cl in c]
    secretVal=[cl.get('secretVal') for cl in c]
    classI=[cl[0] for cl in limit]
    classId=[cl[0].get('teachingClassID') for cl in limit]


    dict1 = dict(zip(teacher, secretVal))
    dict2 = dict(zip(teacher, classId))
    df = pd.DataFrame(list(dict1.items()), columns=['teacher', 'secretVal'])
    df['classId'] = df['teacher'].map(dict2)

    df.to_csv('output.csv', index=False, encoding='utf-8-sig')
    print(df)


# print(dict1)