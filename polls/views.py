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
    message = request.POST
    if message['action'] == 'reg':
        if message['type'] == 'person':
            msg = 'Success register as a person'
            state = 'Success'
        elif message['type'] == 'enterprise':
            msg = 'Success register as a enterprise'
            state = 'Success'
        else:
            state = "Error"
            msg = 'error'
    if message['action'] == 'login':
        if message['type'] == 'person':
            msg = 'Success login as person'
            state = 'Success'
        elif message['type'] == 'enterprise':
            msg = 'Success login as enterprise'
            state = 'Success'
        else:
            state = "Error"
            msg = 'error'
    if message['action'] == 'signup':
        if message['type'] == 'person':
            msg = 'Success sign up as person'
            state = 'Success'
        elif message['type'] == 'enterprise':
            msg = 'Success sign up  as enterprise'
            state = 'Success'
        else:
            state = "Error"
            msg = 'error'
    if message['action'] == 'getPwd':
        print(message)
        if message['type'] == 'person':
            msg = 'Get password as person'
            state = 'Success'
        elif message['type'] == 'enterprise':
            msg = 'Get password  as enterprise'
            state = 'Success'
        else:
            state = "Error"
            msg = 'error'
    data = {
        'state': state,
        'message': {
            'msg': msg
        },
    }
    return HttpResponse(json.dumps(data), content_type="application/json")
