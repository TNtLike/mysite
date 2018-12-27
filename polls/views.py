from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import datetime
import json
from . import testdb
from django.core import serializers


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def polls(request):
    return HttpResponse("Hello, Django. My name is Alex Qiu.")


def home_page(request):
    context = {}
    context['message'] = '{}'.format(datetime.datetime.now())
    return render(request, 'hello.html', context)


def db_add(title, author, context):
    message = testdb.insert(title, author, context)
    return message


def db_show():
    res = testdb.show()
    return res


@csrf_exempt
def getData(request):
    mess = json.loads(request.body)
    m = db_add(mess['title'], mess['author'], mess['context'])

    data = {
        'message': m,
    }
    if request.method == 'GET':
        return HttpResponse(json.dumps(data), content_type="application/json")

    elif request.method == 'POST':
        return HttpResponse(json.dumps(data), content_type="application/json")


@csrf_exempt
def returnData(request):
    info = serializers.serialize('json', db_show())
    # info =  db_show()
    # return HttpResponse(info)
    data = {
        'message': info,
    }
    if request.method == 'GET':
        return HttpResponse(info, content_type="application/json")

    elif request.method == 'POST':
        return HttpResponse(info, content_type="application/json")
