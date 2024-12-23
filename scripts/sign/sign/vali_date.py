validate_url='https://captcha.chaoxing.com/captcha/check/verification/result?callback=cx_captcha_function&captchaId=Qt9FIw9o4pwRjOyqM6yizZBh682qN2TU&type=iconclick&token=FBBE22E675952CC380C8F02249E9DF81&textClickArr=%5B%7B%22x%22%3A233%2C%22y%22%3A122%7D%2C%7B%22x%22%3A275%2C%22y%22%3A85%7D%2C%7B%22x%22%3A67%2C%22y%22%3A117%7D%5D&coordinate=%5B%5D&runEnv=10&version=1.1.20&t=a&iv=39ef589b89b5c5328fbdce44ecfda97c&_=1733842467628'
pic_url='https://captcha.chaoxing.com/captcha/get/verification/image?callback=cx_captcha_function&captchaId=Qt9FIw9o4pwRjOyqM6yizZBh682qN2TU&type=iconclick&version=1.1.20&captchaKey=496a3656e267de2a86588ae19179ae86&token=8d687e72bba83f6f70b4f1f917f4fd05%3A1733842768253&referer=https%3A%2F%2Fmobilelearn.chaoxing.com%2Fpage%2Fsign%2FsignIn%3FcourseId%3D243702828%26classId%3D99786823%26activeId%3D5000112552487%26fid%3D0%26timetable%3D0&iv=4a397a52492e53550b73dcca486d2d09&_=1733842630436'
import requests

def get_pic():
    # 构造 URL 和参数
    base_url = 'https://captcha.chaoxing.com/captcha/get/verification/image'
    params = {
        "callback": "cx_captcha_function",
        "captchaId": "Qt9FIw9o4pwRjOyqM6yizZBh682qN2TU",
        "type": "iconclick",
        "version": "1.1.20",
        "captchaKey": "496a3656e267de2a86588ae19179ae86",
        "token": "8d687e72bba83f6f70b4f1f917f4fd05:1733842768253",
        "referer": "https://mobilelearn.chaoxing.com/page/sign/signIn?courseId=243702828&classId=99786823&activeId=5000112552487&fid=0&timetable=0",
        "iv": "4a397a52492e53550b73dcca486d2d09",
        "_": "1733842630436",
    }
    headers = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "connection": "keep-alive",
        "cookie": "lv=1; fid=200; xxtenc=48014e517761d42180c2a48d1ea2338e; createSiteSource=num8; wfwEnc=E6C78D1111B0057FD2113E77B117CA0F; _uid=237292284; uf=da0883eb5260151e9c23dd4415b963ba59af0e89740d838e58781c0fe448528046678626bc8cd476019e10acad37fc96c49d67c0c30ca5047c5a963e85f110994b0e3a48f60e47c5fd68be96b6183b1af70ce428e898ec978a096e8147bf2e8efab1d3aded52a1d7; _d=1733842068210; UID=237292284; vc=0ABE0A91B328CDFEB0EF6A9899C70169; vc2=70959B0642787FD386134F9BF750E18A; vc3=e4OIg%2BkeSl0p781txAoYrZ81hVFm5KXUkIABH0ijlkFP3xdJCDpPTC38bUTRHICOYQcOZ%2FAq7iot1S5Jz0M9N5Z1b9kXkmhTDy7C95t0ZkoXEjHtRo3PtFbzP5aSWnimJQj7KOsgxoE8KFM6GVh9EcE3X0PDWUxsNs%2F2lXBojBs%3D35427400b95fc530d9d54f2e2c0cd11d; cx_p_token=f042ad6632b13906465784ed11213691; p_auth_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOiIyMzcyOTIyODQiLCJsb2dpblRpbWUiOjE3MzM4NDIwNjgyMTIsImV4cCI6MTczNDQ0Njg2OH0.AOYctUYZDuaIgPAQWmyBttoImuLqwmDpK83DtqoEP2I; DSSTASH_LOG=C_38-UN_1669-US_237292284-T_1733842068212; spaceFid=200; spaceRoleId=3; tl=1; _industry=5; route=c17caf14c9dd9ac7be8390c41e5ffc18; 243702828cpi=263210318; 243702828ut=s; 243702828t=1733842084691; 243702828enc=ed02de995ec8f7f56560fa28eebb277a",
        "host": "captcha.chaoxing.com",
        "referer": "https://mobilelearn.chaoxing.com/page/sign/signIn?courseId=243702828&classId=99786823&activeId=5000112552487&fid=0&timetable=0",
        "sec-ch-ua": '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "script",
        "sec-fetch-mode": "no-cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0",
    }

    try:
        # 发送 GET 请求
        response = requests.get(base_url, params=params,headers=headers, timeout=10)
        response.raise_for_status()  # 检查请求是否成功

        # 返回响应内容
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"请求出错: {e}")
        return None
    
result = get_pic()
if result:
    print(result)