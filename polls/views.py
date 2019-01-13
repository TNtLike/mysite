from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import datetime
import json
from django.core import serializers
from .models import polls_model
from .models import user


def home_page(request):
    context = {}
    context['message'] = '{}'.format(datetime.datetime.now())
    return render(request, 'index.html', context)


# 数据库操作


def insert(title, author, content, type):
    test1 = polls_model(title=title, author=author, content=content, type=type)
    test1.save()
    # return HttpResponse('<p>数据添加成功！</p>')
    return 1


def show():
    list = polls_model.objects.filter().order_by('id')

    # return HttpResponse('<p>'+response+'<p>')
    # return HttpResponse(list)
    return list


def query(id):
    list = polls_model.objects.filter(id=id).order_by('id')

    # return HttpResponse('<p>'+response+'<p>')
    # return HttpResponse(list)
    return list


def delete(id):
    list = polls_model.object.filter(id=id)
    if list.delete():
        return 1
    else:
        return 2


@csrf_exempt
def getData(request):
    mess = json.loads(request.body)
    m = insert(mess['title'], mess['author'], mess['content'], mess['type'])

    data = {
        'message': m,
    }
    if request.method == 'GET':
        return HttpResponse(json.dumps(data), content_type="application/json")

    elif request.method == 'POST':
        return HttpResponse(json.dumps(data), content_type="application/json")


@csrf_exempt
def deleteData(request):
    id = json.loads(request.body)
    m = delete(id['id'])
    if m == 1:
        mess = 'success deleted'
    else:
        mess = 'failed deleted'
    data = {
        'message': mess,
    }
    if request.method == 'GET':
        return HttpResponse(json.dumps(data), content_type="application/json")

    elif request.method == 'POST':
        return HttpResponse(json.dumps(data), content_type="application/json")


@csrf_exempt
def returnSingleData(request):
    id = json.loads(request.body)
    info = serializers.serialize('json', query(id['id']))

    data = {
        'message': info,
    }
    if request.method == 'GET':
        return HttpResponse(info, content_type="application/json")

    elif request.method == 'POST':
        return HttpResponse(info, content_type="application/json")


@csrf_exempt
def returnData(request):
    info = serializers.serialize('json', show())
    # info =  db_show()
    # return HttpResponse(info)
    data = {
        'message': info,
    }
    if request.method == 'GET':
        return HttpResponse(info, content_type="application/json")

    elif request.method == 'POST':
        return HttpResponse(info, content_type="application/json")

# 注册


@csrf_exempt
def submitUser(request):
    message = json.loads(request.body)
    print(message)
    test1 = user(username=message['username'], password=message['password'],
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
    try:
        m = user.objects.get(username=message['username'])
        if m.password == message['password']:
            request.session['username'] = m.username
            info = 1
    except user.DoesNotExist:
        info = 2
    data = {
        'message': info,
    }
    return HttpResponse(json.dumps(data), content_type="application/json")


# 测试
@csrf_exempt
def test(request):
    message = request.POST
    info = 0
    try:
        m = user.objects.get(username=message['username'])
        if m.password == message['password']:
            request.session['username'] = m.username
            info = 1
    except user.DoesNotExist:
        info = 2
    data = {
        'message': info,
    }
    return HttpResponse(json.dumps(data), content_type="application/json")
