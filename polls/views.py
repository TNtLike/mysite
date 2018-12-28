from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import datetime
import json
from django.core import serializers
from .models import polls_model


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def polls(request):
    return HttpResponse("Hello, Django. My name is Alex Qiu.")


def home_page(request):
    context = {}
    context['message'] = '{}'.format(datetime.datetime.now())
    return render(request, 'hello.html', context)


# 数据库操作


def insert(title, author, context, type):
    test1 = polls_model(title=title, author=author, context=context, type=type)
    test1.save()
    # return HttpResponse('<p>数据添加成功！</p>')
    return 1


def show():
    list = polls_model.objects.filter().order_by("id")

    # return HttpResponse('<p>'+response+'<p>')
    # return HttpResponse(list)
    return list


@csrf_exempt
def getData(request):
    mess = json.loads(request.body)
    m = insert(mess['title'], mess['author'], mess['context'], mess['type'])

    data = {
        'message': m,
    }
    if request.method == 'GET':
        return HttpResponse(json.dumps(data), content_type="application/json")

    elif request.method == 'POST':
        return HttpResponse(json.dumps(data), content_type="application/json")


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
