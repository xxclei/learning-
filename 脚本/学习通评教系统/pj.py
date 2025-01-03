import requests

# 目标URL
url = "https://newes.chaoxing.com/pj/newesReceptionV2/GetMyEvaluationList?evaluateObjType=&semesterId=3789&title=&sort=2&pageIndex=1&pageSize=10"
question_url = "https://newes.chaoxing.com/pj/newesReceptionV2/GetMyEvaluationQuestionnaireById"
url_submit = "https://newes.chaoxing.com/pj/newesReception/saveQuestionnaire"
# 请求头
headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-encoding': 'gzip, deflate, br, zstd',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'connection': 'keep-alive',
    'cookie': 'lv=1; xxtenc=48014e517761d42180c2a48d1ea2338e; fname=%u5FAE%u670D%u52A1%u7AD9%u70B9v14; systemId=1600; uname=202283290159; _uid=237292284; UID=237292284; vc=0ABE0A91B328CDFEB0EF6A9899C70169; vc2=B48CAE2E1FCC3E7A6B035726B03A69C3; thirdRegist=0; INGRESSCOOKIE=1735111101.404.22224.695356; uf=da0883eb5260151e9c23dd4415b963ba59af0e89740d838e58781c0fe448528065f4eb1510a4b90b2bbf5f52f3a307d1c49d67c0c30ca5047c5a963e85f110994b0e3a48f60e47c5fd68be96b6183b1af70ce428e898ec97cadc21e5a4435e52f9b386d93644725b; _d=1735124641753; vc3=cn%2Frj6v4gImC03tjswkL9F8qcMZxWEMZ6dE7R7dtAakk8XUx48pva68b4HL%2FEcvvjLe7oi0ZBxAV62pFfmPxUic1Y%2B1hq7CNqQP6WEleB4qtaUxWmxgE3z%2Bc2ccq8rQr6YQPXgw%2B8J6eu6Quc5x8cPXc2cMbdkXJdeSzYlKa0t4%3D2e4e55551e9917799c8722d83b7ef2ae; cx_p_token=2ca7f193ac87fb8d5e590ed47da53f2f; p_auth_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOiIyMzcyOTIyODQiLCJsb2dpblRpbWUiOjE3MzUxMjQ2NDE3NTUsImV4cCI6MTczNTcyOTQ0MX0.n77aTGtD_Z6jOOrIR2cl_JW31wGkhal_Me8Rkw0X2jw; DSSTASH_LOG=C_38-UN_1669-US_237292284-T_1735124641755; createSiteSource=num8; source=num8; wfwEnc=E6C78D1111B0057FD2113E77B117CA0F; tl=1; spaceFid=250111; spaceRoleId=""; fid=250111; jrose=28BDBC388093978CF776FB7436D046B6.ans; route=efbdef9576ec2207e9f18266c876393d',
    'host': 'newes.chaoxing.com',
    'referer': 'https://newes.chaoxing.com/pj/frontv2/evaluateList/whatIEvaluated?_CP_=pj',
    'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0'
}

# 发送GET请求
response = requests.get(url, headers=headers)


questionnaire_ids=[]
questionnaires_details={"alreadyId":[],
                        "grantId":[],
                        'questionnaireId':[]
}


def get_questionnaire_ids():
# 检查响应状态码
    if response.status_code == 200:
        print("请求成功，状态码：", response.status_code)
        # 打印响应内容
        res=response.json()
        res_list=res.get("data").get("list")
        for questionnaire in res_list:
            print(questionnaire["questionnaireId"])
            questionnaire_ids.append(questionnaire["questionnaireId"])
            
    else:
        print("请求失败，状态码：", response.status_code)
def get_questionnaires():
    # URL参数
    for questionnaireId in questionnaire_ids:
        params = {
            'questionnaireId': questionnaireId,  # 问卷ID
            'pageIndex': 1,                # 页码
            'pageSize': 11,                # 每页大小
            'kw': ''                      # 关键词
        }
        # 发送GET请求
        response = requests.get(question_url, params=params, headers=headers)

        # 检查响应状态码
        if response.status_code == 200:
            # print("请求成功，状态码：", response.status_code)
            # 打印响应内容
            res=response.json()['data']['list']
            for r in res:
                print(r['alreadyObject']['alreadyName']+" "+r['alreadyObject']['courseName'])
        
                questionnaires_details['questionnaireId'].append(questionnaireId)
                questionnaires_details['alreadyId'].append(r['alreadyObjectId'])
                questionnaires_details['grantId'].append(r['grantId'])
        else:
            print("请求失败，状态码：", response.status_code)
def submit_questionnaire(questionnaireId=0,alreadyId=0,grantId=0,groupTargetIds=0):
    data = {
    'uId': 237292284,
    'fid': 250111,
    'questionnaireId': questionnaireId,
    'alreadyId': alreadyId,
    'grantId': grantId,
    'groupTargetIds': 965285,
    '965285_type': 5,
    '965285_chooseSetUp': 1,
    '965285': 10,

    'groupTargetIds': 965286,
    '965286_type': 5,
    '965286_chooseSetUp': 1,
    '965286': 10,
    'groupTargetIds': 965287,
    '965287_type': 5,
    '965287_chooseSetUp': 1,
    '965287': 10,
    'groupTargetIds': 965288,
    '965288_type': 5,
    '965288_chooseSetUp': 1,
    'groupTargetIds': 965289,
    '965289_type': 5,
    '965289_chooseSetUp': 1,
    '965289': 10,
   
    'groupTargetIds': 965290,
    '965290_type': 5,
    '965290_chooseSetUp': 1,
    '965290': 10,
    'groupTargetIds': 965291,
    '965291_type': 5,
    '965291_chooseSetUp': 1,
    '965291': 10,
    'groupTargetIds': 965292,
    '965292_type': 5,
    '965292_chooseSetUp': 1,
    '965292': 10,
    'groupTargetIds': 965293,
    '965293_type': 5,
    '965293_chooseSetUp': 1,
    '965293': 10,
    'groupTargetIds': 965294,

    '965294_type': 5,
    '965294_chooseSetUp': 1,
    '965294': 10,
    'groupTargetIds': 965295,
    '965295_type': 5,
    '965295_chooseSetUp': 1,
    '965295': 10,
    'groupTargetIds': 965296,

    '965296_type': 5,
    '965296_chooseSetUp': 1,
    '965296': 10,
    'groupTargetIds': 965297,
    '965297_type': 5,
    '965297_chooseSetUp': 1,
    '965297': 10,
    'groupTargetIds': 965298,
    '965298_type': 5,
    '965298_chooseSetUp': 1,
    '965298': 10,
    'groupTargetIds': 965299,
    

    '965299_type': 5,
    '965299_chooseSetUp': 1,
    '965299': 10,
    'groupTargetIds': 965300,
    '965300_type': 5,
    '965300_chooseSetUp': 1,
    '965300': 10,
    'groupTargetIds': 965301,
    '965301_type': 5,
    '965301_chooseSetUp': 1,
    '965301': 10,
    'groupTargetIds': 965302,
    '965302_type': 5,
    '965302_chooseSetUp': 1,
    '965302': 10,
    'groupTargetIds': 965303,
    '965303_type': 5,
    '965303_chooseSetUp': 1,
    '965303': 10,
    'groupTargetIds': 965304,
    '965304_type': 5,
    '965304_chooseSetUp': 1,
    '965304': 10,
    'groupTargetIds': 965305,
    '965305_type': 5,
    '965305_chooseSetUp': 1,
    '965305': 10,
    'groupTargetIds': 965306,
    '965306_type': 5,
    '965306_chooseSetUp': 1,
    '965306': 10,
    'groupTargetIds': 965307,
    '965307_type': 5,
    '965307_chooseSetUp': 1,
    '965307': 10,
    'groupTargetIds': 965308,
    '965308_type': 5,
    '965308_chooseSetUp': 1,
    '965308': 10,
    'saveType': 2,
    
    'submitreasons': '',
    'submit_highscore_reasons': '',
    'submit_lowscore_reasons': ''
    }



    # 发送POST请求
    response = requests.post(url=url_submit, data=data, headers=headers)

    # 检查响应状态码
    if response.status_code == 200:
        print("请求成功，状态码：", response.status_code)
        # 打印响应内容
        print(response.text)
    else:
        print("请求失败，状态码：", response.status_code)


get_questionnaire_ids()
get_questionnaires()
print(questionnaires_details)

# for i in range(0,len(questionnaires_details['alreadyId'])):
#     alreadyId=questionnaires_details['alreadyId'][i]
#     grantId=questionnaires_details['grantId'][i]
#     questionnaireId=questionnaires_details['questionnaireId'][i]
#     submit_questionnaire(questionnaireId,alreadyId,grantId)

