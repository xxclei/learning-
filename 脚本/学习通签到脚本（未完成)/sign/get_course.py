from bs4 import BeautifulSoup
import re


url_course="https://i.chaoxing.com/base?t=1733740710766"

def get_native_course():
    # 读取存储网页内容的 txt 文件
    with open('html.txt', 'r', encoding='utf-8') as file:
        content = file.read()

    # 使用 BeautifulSoup 解析 HTML 内容
    soup = BeautifulSoup(content, 'html.parser')
    
    # 创建二维数组存储提取的课程信息
    course_data = []

    # 遍历每个课程块
    courses = soup.find_all('h3', class_='inlineBlock')
    for course in courses:
       
        # 提取课程名
        course_name_tag = course.find('span', class_='course-name')
        course_name = course_name_tag['title'] if course_name_tag else '未知课程名'

        # 提取 course_id 和 class_id
        link_tag = course.find('a', class_='color1')
        if link_tag and 'href' in link_tag.attrs:
            link = link_tag['href']
            # 使用正则表达式提取参数
            course_id = re.search(r'courseid=(\d+)', link)
            class_id = re.search(r'clazzid=(\d+)', link)
            course_id = course_id.group(1) if course_id else '未知ID'
            class_id = class_id.group(1) if class_id else '未知ID'
        else:
            course_id, class_id = '未知ID', '未知ID'

        # 将提取的信息存入二维数组
        course_data.append([course_id, class_id, course_name])

    return course_data
get_native_course()