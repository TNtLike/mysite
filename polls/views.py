from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import datetime
import json
from django.core import serializers
from .models import person
from .models import person_resume
from .models import enterprise
from .models import enterprise_jobs


def home_page(request):
    context = {}
    context['message'] = '{}'.format(datetime.datetime.now())
    return render(request, 'index.html', context)


def hello(request):
    context = {}
    context['message'] = '{}'.format(datetime.datetime.now())
    return render(request, 'hello.html', context)


# 个人用户注册
@csrf_exempt
def submitUser(request):
    message = json.loads(request.body)
    print(message)
    test1 = person(username=message['username'], password=message['password'],
                   question=message['question'], answer=message['answer'], email=message['email'],)
    if test1.save():
        info = 'failed'
    else:
        info = 'success'
    data = {
        'message': info,
    }
    if request.method == 'GET':
        return HttpResponse(json.dumps(data), content_type="application/json")

    elif request.method == 'POST':
        return HttpResponse(json.dumps(data), content_type="application/json")


# 登录
@csrf_exempt
def login(request):
    message = json.loads(request.body)
    info = 0
    username = ''
    try:
        m = person.objects.get(username=message['username'])
        if m.password == message['password']:
            # request.session['username'] = m.username
            info = 1
            username = m.username
    except person.DoesNotExist:
        info = 2
    data = {
        'message': info,
        'username': username
    }
    return HttpResponse(json.dumps(data), content_type="application/json")


# 测试
@csrf_exempt
def test(request):
    worksInfo = [{
        'companyName': "宁波智士网络科技有限公司",
        'industry': "计算机软件",
        'department': "开发部门",
        'position': "前端开发工程师",
        'description': "11111111111111111111",
    }]
    edusInfo = [{
        'school': "长春工程学院",
        'major': "计算机科学与技术",
        'degree': "本科",
        'gradTime': "2019",
    }]
    projectsInfo = [{
        'projectname': "网站",
        'org': "宁波智士网络科技有限公司",
        'position': "开发部门",
        'description': "前端开发",
        'duty': "开发",
    }]
    skillsInfo = [{
        'skillName': "英语",
        'proficiency': "精通",
        'skillType': "语言",
    }]
    othersInfo = [{
        'content': "ACM",
    }]
    personInfo = {
        'name': '王小明',
        'sex': '男',
        'loca': '宁波',
        'workYear': '2015-02',
        'email': '987073656@qq.com',
        'tel': '13252466597',

    }
    baseInfo = {
        'loca': '宁波',
        'workState': '离职',
        'birth': '1997-01',
        'marriage': '未婚'
    }
    jobIntentInfo = {
        'pay': '100',
        'loca': '宁波',
        'industry': '计算机信息技术',
        'function': 'web前端开发',
        'arrTime': '一月内',
        'introduction': 'onsljlzlmklamscopmasa;lsmdl;asojkdapoksd;lmsdoajsdioansaloimspo'
    }

    if request.method == 'GET':
        data = {
            'personInfo': personInfo,
            'baseInfo': baseInfo,
            'jobIntentInfo': jobIntentInfo,
            'worksInfo': worksInfo,
            'edusInfo': edusInfo,
            'projectsInfo': projectsInfo,
            'skillsInfo': skillsInfo,
            'othersInfo': othersInfo,
        }
        
        return HttpResponse(json.dumps(data), content_type="application/json")
    elif request.method == 'POST':

        message = request.POST
        print(message)
        action = message['action']
        d = message['data']
        if action == 'edit_personInfo':
            personInfo=eval(d)
        elif action == 'edit_baseInfo':
            baseInfo=eval(d)
        elif action == 'edit_jobIntentInfo':
            jobIntentInfo=eval(d)
        elif message['action'] == 'add_workInfo':
            worksInfo.append(eval(d))
            print(worksInfo)
        elif message['action'] == 'del_workInfo':
            print(eval(d))
            
            print(worksInfo)
            # worksInfo.pop(eval(d))
        data2 = {
            'msg': 1,
            'personInfo': personInfo,
            'baseInfo': baseInfo,
            'jobIntentInfo': jobIntentInfo,
            'worksInfo': worksInfo,
            'edusInfo': edusInfo,
            'projectsInfo': projectsInfo,
            'skillsInfo': skillsInfo,
            'othersInfo': othersInfo,
        }
        return HttpResponse(json.dumps(data2), content_type="application/json")
    # if message = request.POST:
    # if message['action'] == 'reg':
    #     if message['type'] == 'person':
    #         msg = 'Success register as a person'
    #         state = 'Success'
    #     elif message['type'] == 'enterprise':
    #         msg = 'Success register as a enterprise'
    #         state = 'Success'
    #     else:
    #         state = "Error"
    #         msg = 'error'
    # if message['action'] == 'login':
    #     if message['type'] == 'person':
    #         msg = 'Success login as person'
    #         state = 'Success'
    #     elif message['type'] == 'enterprise':
    #         msg = 'Success login as enterprise'
    #         state = 'Success'
    #     else:
    #         state = "Error"
    #         msg = 'error'
    # if message['action'] == 'signup':
    #     if message['type'] == 'person':
    #         msg = 'Success sign up as person'
    #         state = 'Success'
    #     elif message['type'] == 'enterprise':
    #         msg = 'Success sign up  as enterprise'
    #         state = 'Success'
    #     else:
    #         state = "Error"
    #         msg = 'error'
    # if message['action'] == 'getPwd':
    #     print(message)
    #     if message['type'] == 'person':
    #         msg = 'Get password as person'
    #         state = 'Success'
    #     elif message['type'] == 'enterprise':
    #         msg = 'Get password  as enterprise'
    #         state = 'Success'
    #     else:
    #         state = "Error"
    #         msg = 'error'
    # data = {
    #     'state': state,
    #     'message': {
    #         'msg': msg
    #     },
    # }
    # return HttpResponse(json.dumps(data), content_type="application/json")
