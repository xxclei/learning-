import requests
import json


from bs4 import BeautifulSoup
from get_course import get_native_course

# 设置请求的 URL
base_url = "https://mobilelearn.chaoxing.com/v2/apis/active/student/activelist?fid=0&courseId={courseId}&classId={classId}&showNotStartedActive=0&_={timestamp}"
url_getactive="https://mobilelearn.chaoxing.com/v2/apis/active/student/activelist?fid=0&courseId=248582749&classId=111526610&showNotStartedActive=0&_=1733707491691"
url_sign = "https://mobilelearn.chaoxing.com/v2/apis/sign/signIn?activeId={activeId}"
url_course = 'https://mooc1-1.chaoxing.com/visit/interaction?s=0f4ce38f2606d3bdd14bc60190f7c734'
sign_verti='https://mobilelearn.chaoxing.com/widget/sign/pcStuSignController/checkIfValidate?DB_STRATEGY=PRIMARY_KEY&STRATEGY_PARA=activeId&activeId={activeId}&puid='
# 设置请求参数
params = {
    'activeId': '6000110744282',
    'signCode': '',
    'validate': 'validate_Qt9FIw9o4pwRjOyqM6yizZBh682qN2TU_47C4A8D69C730C9C61BC96124E2A044F',
    'moreClassAttendEnc': ''
}

# 设置请求头
headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Cookie': 'lv=1; fid=200; xxtenc=48014e517761d42180c2a48d1ea2338e; createSiteSource=num8; wfwEnc=E6C78D1111B0057FD2113E77B117CA0F; _uid=237292284; uf=da0883eb5260151e9c23dd4415b963ba59af0e89740d838e58781c0fe4485280b347a871fbe644ea6a02c777a3756cd6c49d67c0c30ca5047c5a963e85f110994b0e3a48f60e47c5fd68be96b6183b1af70ce428e898ec97e88a099322cf7c928c264d3b8b2bcbd6; _d=1733706849846; UID=237292284; vc=0ABE0A91B328CDFEB0EF6A9899C70169; vc2=69C5A8CF662590AC959C0598E3F6EA85; vc3=VSARwjemjucQ%2FR1pV6dePeGn3hyF8GYO1B9XRNfeFZq1XiUHg7pX%2Fsqff2%2BCaBQjU%2FgoIeFA7QF5%2BVw8Wu1g1JrJvOxgFN5S4PNcp6SwMKFkHxVdMJ4PlsZylO%2Fa1dU3vgaCZWLaupu8Kg5DBJTJqS3qRXcxz3%2Bp%2BiBvIWq91Ys%3Da293e2943bc2e6f1abcaf74fe08cf185; cx_p_token=38432b17fd0689e4f22bade868f7e003; p_auth_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOiIyMzcyOTIyODQiLCJsb2dpblRpbWUiOjE3MzM3MDY4NDk4NDcsImV4cCI6MTczNDMxMTY0OX0.ooIXNtZD1RVuYRoNqpV73A7Q-wHo2c2orOoredxQvog; DSSTASH_LOG=C_38-UN_1669-US_237292284-T_1733706849847; source=num8; spaceFid=200; spaceRoleId=3; tl=1; route=2148913a4cfb9c1702825d3c604f8740; JSESSIONID=E435029C6E816AEEFF0A83EE88BEB38D; route_mobilelearn=3e8fc13b01a0f202fcd2ef01bdd0177a; route_widget=a1ed9e22c22d0fc4105652d9b8f2f447',
    'Host': 'mobilelearn.chaoxing.com',
    'Referer': 'https://mobilelearn.chaoxing.com/page/sign/signIn?courseId=248582749&classId=111526610&activeId=6000110744282&fid=0&timetable=0',
    'Sec-Ch-Ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
    'X-Requested-With': 'XMLHttpRequest'
}

data = {
    'username': '18921544758',  # 用户名字段
    'password': 'xc591730',  # 密码字段
    # 可能还需要其他字段，如验证码或CSRF令牌
}

def generate_urls(course_data, base_url):
    t = int(time.time() * 1000)  # 获取毫秒级的时间戳
    url_list = []
    
    for course1 in course_data:
        # print(course1)
        course_id = course1[0]  # 获取 course_id
        class_id = course1[1]   # 获取 class_id
        
        # 使用 base_url 模板生成完整的 URL
        url = base_url.format(courseId=course_id, classId=class_id, timestamp=t)
        print(url)
        
        # 将生成的 URL 添加到列表中
        url_list.append(url)

    return url_list


def generate_url(course_data, base_url,t):
     t= int(time.time() * 1000)  # 获取毫秒级的时间戳


def get_active_id(url_g):
    # 发起 GET 请求
    response = requests.get(url_g, params=params, headers=headers)
    res=response.json()
    # print(res)
    active_list = res['data']['activeList'] # 提取活动列表
    act_list= [[a['id'],a['nameOne']]for a in active_list]
    # print(active_list)
    # 打印响应内容
    if response.status_code == 200:
        print("请求成功，返回内容：")
        # print(response.json())
        # print(act_list )
        return act_list
    else:
        print(f"请求失败，状态码：{response.status_code}")
        return False
    
def login_and_get_courses(course_url, data):
    # 创建一个Session对象，用于保持会话
    # session = requests.Session()

    # 设置请求头，模拟浏览器请求
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
  
        #  "Host":"mooc1-1.chaoxing.com",
         "origin":"https://mooc1-1.chaoxing.com",
    "Referer": "https://mooc1-1.chaoxing.com/visit/interaction?s=0f4ce38f2606d3bdd14bc60190f7c734",
    # Add Cookie here
    "Cookie": "orgfid=43843; registerCode=00010048000100010018; lv=1; fid=200; _uid=237292284; UID=237292284; vc=0ABE0A91B328CDFEB0EF6A9899C70169; vc2=69C5A8CF662590AC959C0598E3F6EA85; xxtenc=48014e517761d42180c2a48d1ea2338e; spaceFid=200; spaceRoleId=3; tl=1; createSiteSource=""; source=""; wfwEnc=B167B4BFE900674986E6F61F16521B01; thirdRegist=0; fanyamoocs=3835A68B259ECAF901A2650E5D0A921A; uf=da0883eb5260151e9c23dd4415b963ba59af0e89740d838e58781c0fe448528048aa803c29db50c47d9e277f88c4a9ddc49d67c0c30ca5047c5a963e85f110994b0e3a48f60e47c5fd68be96b6183b1af70ce428e898ec97acda2e72eb1b4e9d22c096fb0c35fca0; _d=1733734358849; vc3=Qv8RtUP0arRGVV%2FFW%2Faxu1bR6UROF0Wno1Zh4feITUA5fxPqxoSJ2NB63FItTAa2XL59uqjYLzlYpU5%2FUk9uQsXvT1ocfAS7vw1pnM5DpFFnlSiIvFnLm7SB%2BlmYAfKsEQvWuqKjC6bqLsWfFUo6LlsEy6RYDIm4b4%2B%2BSfTp95Q%3D14d2f0067b06f560943c71840feb622a; cx_p_token=a7c85c685961091d7c117de1230f367a; p_auth_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOiIyMzcyOTIyODQiLCJsb2dpblRpbWUiOjE3MzM3MzQzNTg4NTAsImV4cCI6MTczNDMzOTE1OH0.w_doD9QMnuCSzdc5rxDL8a-_kqFjkCxQ_rUC7VeHuz8; DSSTASH_LOG=C_38-UN_1669-US_237292284-T_1733734358851; k8s=1733734408.899.202.631887; jrose=78208814D779A428A80F069D433F7F3A.mooc-2189577418-2529q; route=f9c314690d8e5d436efa7770254d0199; _industry=5; _dd237292284=1733734735981"
    }
    course_response = requests.post(course_url, headers=headers)
    
    if course_response.status_code == 200:
        print("获取课程数据成功，正在解析...")
        html = course_response.text
        print(html)
        soup = BeautifulSoup(html, 'html.parser')

        # 初始化一个空列表，用于存储课程名称和courseId
        course_list = []

        # 查找所有课程项
        courses = soup.find_all('div', class_='course')

        # 遍历课程项并提取课程名称和ID
        for course in courses:
            # 获取课程名称
            course_name = course.find('span', class_='course-name').get_text(strip=True)
            
            # 获取courseId
            course_id = course.find('input', class_='courseId')['value']
            
            # 将课程名称和courseId以列表的形式加入到course_list中
            course_list.append([course_name, course_id])
            
        return course_list
    else:
        print(f"获取课程数据失败，状态码：{course_response.status_code}")
        return []
#未实现


def sign_complex(active_id):
     header2s = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Encoding': 'gzip, deflate, br, zstd',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Cookie': 'lv=1; fid=200; _uid=237292284; UID=237292284; vc=0ABE0A91B328CDFEB0EF6A9899C70169; vc2=69C5A8CF662590AC959C0598E3F6EA85; xxtenc=48014e517761d42180c2a48d1ea2338e; tl=1; createSiteSource=""; wfwEnc=B167B4BFE900674986E6F61F16521B01; uf=da0883eb5260151e9c23dd4415b963ba59af0e89740d838e58781c0fe448528048aa803c29db50c47d9e277f88c4a9ddc49d67c0c30ca5047c5a963e85f110994b0e3a48f60e47c5fd68be96b6183b1af70ce428e898ec97acda2e72eb1b4e9d22c096fb0c35fca0; _d=1733734358849; vc3=Qv8RtUP0arRGVV%2FFW%2Faxu1bR6UROF0Wno1Zh4feITUA5fxPqxoSJ2NB63FItTAa2XL59uqjYLzlYpU5%2FUk9uQsXvT1ocfAS7vw1pnM5DpFFnlSiIvFnLm7SB%2BlmYAfKsEQvWuqKjC6bqLsWfFUo6LlsEy6RYDIm4b4%2B%2BSfTp95Q%3D14d2f0067b06f560943c71840feb622a; cx_p_token=a7c85c685961091d7c117de1230f367a; p_auth_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOiIyMzcyOTIyODQiLCJsb2dpblRpbWUiOjE3MzM3MzQzNTg4NTAsImV4cCI6MTczNDMzOTE1OH0.w_doD9QMnuCSzdc5rxDL8a-_kqFjkCxQ_rUC7VeHuz8; DSSTASH_LOG=C_38-UN_1669-US_237292284-T_1733734358851; _industry=5; thirdRegist=0; fanyamoocs=3835A68B259ECAF901A2650E5D0A921A; route=5f4c1fdb37f0b16738faa91aa181cd52; JSESSIONID=A8F3EE210E33942E374EA3C9DE838E86; route_mobilelearn=3e8fc13b01a0f202fcd2ef01bdd0177a; route_widget=8229b6d3fc4e930470a4554052d4779e',
            'Host': 'mobilelearn.chaoxing.com',
            'Sec-Ch-Ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': '"Windows"',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'Referrer-Policy': 'unsafe-url',
            'Origin-Agent-Cluster': '?0',
            'X-Requested-With': 'XMLHttpRequest'
        }
     print(sign_verti.format(activeId=active_id))
     response = requests.get(sign_verti.format(activeId=active_id), headers=header2s, proxies=None)
     if response.status_code == 200:
        print("签到成功：")
        print(str(response.json().get('msg'))+str(response.json().get('errorMsg')))
        return True
     else:
        print(f"请求失败，状态码：{response.status_code}")
        print(response.text)
        return False
    
import time

def sign(active_id):
     header2s = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Encoding': 'gzip, deflate, br, zstd',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Cookie': 'lv=1; fid=200; _uid=237292284; UID=237292284; vc=0ABE0A91B328CDFEB0EF6A9899C70169; vc2=69C5A8CF662590AC959C0598E3F6EA85; xxtenc=48014e517761d42180c2a48d1ea2338e; tl=1; createSiteSource=""; wfwEnc=B167B4BFE900674986E6F61F16521B01; uf=da0883eb5260151e9c23dd4415b963ba59af0e89740d838e58781c0fe448528048aa803c29db50c47d9e277f88c4a9ddc49d67c0c30ca5047c5a963e85f110994b0e3a48f60e47c5fd68be96b6183b1af70ce428e898ec97acda2e72eb1b4e9d22c096fb0c35fca0; _d=1733734358849; vc3=Qv8RtUP0arRGVV%2FFW%2Faxu1bR6UROF0Wno1Zh4feITUA5fxPqxoSJ2NB63FItTAa2XL59uqjYLzlYpU5%2FUk9uQsXvT1ocfAS7vw1pnM5DpFFnlSiIvFnLm7SB%2BlmYAfKsEQvWuqKjC6bqLsWfFUo6LlsEy6RYDIm4b4%2B%2BSfTp95Q%3D14d2f0067b06f560943c71840feb622a; cx_p_token=a7c85c685961091d7c117de1230f367a; p_auth_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOiIyMzcyOTIyODQiLCJsb2dpblRpbWUiOjE3MzM3MzQzNTg4NTAsImV4cCI6MTczNDMzOTE1OH0.w_doD9QMnuCSzdc5rxDL8a-_kqFjkCxQ_rUC7VeHuz8; DSSTASH_LOG=C_38-UN_1669-US_237292284-T_1733734358851; _industry=5; thirdRegist=0; fanyamoocs=3835A68B259ECAF901A2650E5D0A921A; route=5f4c1fdb37f0b16738faa91aa181cd52; JSESSIONID=A8F3EE210E33942E374EA3C9DE838E86; route_mobilelearn=3e8fc13b01a0f202fcd2ef01bdd0177a; route_widget=8229b6d3fc4e930470a4554052d4779e',
            'Host': 'mobilelearn.chaoxing.com',
            'Sec-Ch-Ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': '"Windows"',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'Referrer-Policy': 'unsafe-url',
            'Origin-Agent-Cluster': '?0',
            'X-Requested-With': 'XMLHttpRequest'
        }
     print(url_sign.format(activeId=active_id))
     response = requests.get(url_sign.format(activeId=active_id), headers=header2s, proxies=None)
     if response.status_code == 200:
        print("签到成功：")
        print(str(response.json().get('msg'))+str(response.json().get('errorMsg')))
        return True
     else:
        print(f"请求失败，状态码：{response.status_code}")
        print(response.text)
        return False
    
import time


def update_courses():#将html文件的txt中courseid提取出来
   
    courses=get_native_course()
    with open("courses.txt", "w", encoding="utf-8") as file:
        for item in courses:
            file.write(str(item) + "\n")  # 每个列表元素单独写入一行

    print("update_courses_success")


def get_():

    url_list = generate_urls(courses, base_url)
    for i in range(0,len(courses)-1):
        print(courses[i])
        # print(url_list[i])
        active_id=get_active_id(url_list[i])
        courses.append(active_id)
        print("共有"+str(len(active_id))+"条签到")
    print(courses)


def load_courses():
    courses = []
    with open("courses.txt", "r", encoding="utf-8") as file:
        for line in file:
            # 去除行尾空白字符后，使用 split() 按空格分割
            parts = line.strip().split()
            # 清理每个部分，去除多余的引号或括号
            cleaned_parts = [part.strip("[]',") for part in parts]
            # 将清理后的数据添加到 courses 列表中
            courses.append(cleaned_parts)
    return courses


def load_classes():
    courses = []
    with open("classes.txt", "r", encoding="utf-8") as file:
        for line in file:
            # 去除行尾空白字符后，使用 split() 按空格分割
            parts = line.strip().split()
            # 清理每个部分，去除多余的引号或括号
            cleaned_parts = [part.strip("[]',") for part in parts]
            # 将清理后的数据添加到 courses 列表中
            courses.append(cleaned_parts)
    return courses


# update_courses()
courses=load_courses()#从本地读取课程列表
classes=load_classes()
active_url=generate_urls(course_data=classes,base_url=base_url)#从coursesid中获取存在的签到界面url


# while(True):
#     time.sleep(1)
#     for url in active_url:
#         active_list=get_active_id(url)
#         for active in active_list:
#             print(active)
#             sign(active[0])#签到

sign_complex(5000112552487)

# active_id=get_active_id(active_url)
# print(active_id)
# sign(5000112399443)

# # 打印结果
# if courses:
#     print("获取的课程信息：")
#     for course in courses:
#         print(course)


# active_id=get_active_id()
# print(active_id)