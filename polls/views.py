from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import datetime
import json
from django.core import serializers

# email
from django.core.mail import EmailMessage

from .models import psn
from .models import psn_resume
from .models import ent
from .models import ent_jobs
from .models import ent_baseInfo


# 个人用户注册
@csrf_exempt
def submitUser(request):
    message = json.loads(request.body)
    save_new_psn = psn(username=message['username'], password=message['password'],
                       question=message['question'], answer=message['answer'], email=message['email'],)
    if save_new_psn.save():
        info = 'error'
        msg = '注册失败'
    else:
        info = 'ok'
        msg = '注册成功'
    data = {
        'status': info,
        'msg': msg
    }
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
            request.session['isLogin'] = True
            request.session['username'] = m.username
            request.session['userId'] = m.id
            info = 1
            username = m.username
    except person.DoesNotExist:
        info = 2
    data = {
        'status': info,
        # 'username': username
    }
    return HttpResponse(json.dumps(data), content_type="application/json")

# 身份校验

# 测试


@csrf_exempt
def test(request):
    worksInfo = [{
        'companyName': "宁波智士网络科技有限公司",
        'industry': "计算机软件",
        'location': "宁波",
        'workTime': "2019-02 - 2019-03",
        'department': "开发部门",
        'position': "前端开发工程师",
        'pay': '122222',
        'description': "11111111111111111111",
    }]
    edusInfo = [{
        'school': "长春工程学院",
        'major': "计算机科学与技术",
        'degree': "本科",
        'gradTime': "2019",
        'transfer': True,
        'overseas': False,
    }]
    projectsInfo = [{
        'projectName': "网站",
        'projectTime': "2018-02 - 2018-03",
        'score': "qwefdwdf",
        'description': "前端开发",
        'duty': "开发",
    }]
    skillsInfo = [{
        'skillName': "铸造工艺",
        'proficiency': "精通",
    }]
    langsInfo = [{
        'type': "英语",
        'proficiency': "简单沟通",
    }]
    othersInfo = [{
        'content': "ACM",
    }]
    tags = [{
        'name': "项目管理",
        'value': True
    }, {
        'name': "123",
        'value': True
    }, {
        'name': "123333",
        'value': False
    }]
    baseInfo = {
        'name': '王小明',
        'sex': '男',
        'location': '宁波',
        'industry': '计算机软件',
        'function': 'web全栈开发',
        'position': '前端开发',
        'companyName': '宁波智士网络科技有限公司',
        'startWork': '2015'
    }
    personInfo = {
        'location': '宁波',
        'workState': '离职',
        'birth': '1997-01',
        'marriage': '未婚'
    }
    jobIntentInfo = {
        'pay': '面议',
        'location': '宁波',
        'industry': '其他',
        'function': 'web前端开发',
        'type': '全职',
        'introduction': 'ofaefaafamadsmalsmdalkmsdlqwodqpwoekpoqwkepoqkweqpwoekqpwosefspmfslkmcvxlmlkmekpqowkeqwpokokznsljlzlmklamscopmasa;lsmdl;asojkdapoksd;lmsdoajsdioansaloimspo'
    }

    if request.method == 'GET':
        print(person_baseInfo.objects.get(id=1).name)
        data = {
            'personInfo': personInfo,
            'baseInfo': baseInfo,
            'jobIntentInfo': jobIntentInfo,
            'tags': tags,
            'worksInfo': worksInfo,
            'edusInfo': edusInfo,
            'projectsInfo': projectsInfo,
            'skillsInfo': skillsInfo,
            'langsInfo': langsInfo,
            'othersInfo': othersInfo,
        }

        return HttpResponse(json.dumps(data), content_type="application/json")
    elif request.method == 'POST':

        message = request.POST
        print(message)
        action = message['action']
        d = message['data']
        if action == 'edit_personInfo':
            personInfo = eval(d)
        elif action == 'edit_baseInfo':
            edit_baseInfo = person_baseInfo(name=eval(d)['name'], sex=eval(d)['sex'],
                                            location=eval(d)['location'], industry=eval(d)['industry'], position=eval(d)['position'], function=eval(d)['function'], companyName=eval(d)['companyName'], startWork=eval(d)['startWork'])
            edit_baseInfo.save()
            baseInfo = eval(d)
        elif action == 'edit_jobIntentInfo':
            jobIntentInfo = eval(d)
        elif message['action'] == 'add_skillInfo':
            skillsInfo.append(eval(d))
            print(skillsInfo)
        elif message['action'] == 'add_langInfo':
            langsInfo.append(eval(d))
            print(langsInfo)
        elif message['action'] == 'add_workInfo':
            worksInfo.append(eval(d))
            print(worksInfo)

        elif message['action'] == 'add_eduInfo':
            edusInfo.append(eval(d))
            print(edusInfo)

        elif message['action'] == 'edit_workInfo':
            print(eval(d))
            index = eval(message['index'])
            worksInfo[index] = eval(d)
        elif message['action'] == 'edit_eduInfo':
            print(d)
            # index = eval(message['index'])
            # edusInfo[index] = eval(d)
        elif message['action'] == 'edit_skillInfo':
            print(eval(d))
            index = eval(message['index'])
            skillsInfo[index] = eval(d)
        elif message['action'] == 'del_workInfo':
            print(eval(d))

            print(worksInfo)
            # worksInfo.pop(eval(d))
        data2 = {
            'state': 'success',
            'personInfo': personInfo,
            'baseInfo': baseInfo,
            'jobIntentInfo': jobIntentInfo,
            'worksInfo': worksInfo,
            'edusInfo': edusInfo,
            'projectsInfo': projectsInfo,
            'skillsInfo': skillsInfo,
            'langsInfo': langsInfo,
            'othersInfo': othersInfo,
        }
        return HttpResponse(json.dumps(data2), content_type="application/json")


# 测试
@csrf_exempt
def test3(request):
    mssg = request.POST
    print(mssg)
    # msg = json.loads(request.POST.param)

    data2 = {
        'state': 'ok',
        'msg': '1',
        'userid': '2'
    }
    return HttpResponse(json.dumps(data2), content_type="application/json")


# 发送邮件测试
@csrf_exempt
def test4(request):
    title = u'邮件主题'
    host = 'qiulangcheng@qlcnb.club'
    resHost = ['qiulangcheng@gmail.com']
    html_content = "<h2>Here is the message.</h2> <p>This is a test email from <a href='qlcnb.club'>qlcnb.club</a>.</p> <p>You can visit our website without sign up an account</p>"
    email = EmailMessage(title, html_content, host, resHost)
    email.content_subtype = "html"
    email.send()
    return HttpResponse("hello World!")
