from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import datetime
import json
from . import testdb


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def polls(request):
    return HttpResponse("Hello, Django. My name is Alex Qiu.")


def home_page(request):
    context = {}
    context['message'] = '{}'.format(datetime.datetime.now())
    return render(request, 'hello.html', context)


def db_add(name, age, sex, tel):
    message = testdb.insert(name, age, sex, tel)
    return message


def db_show():
    response = testdb.show()
    return response


@csrf_exempt
def getData(request):
    mess = json.loads(request.body)
    m = db_add(mess['name'], mess['age'], mess['sex'], mess['tel'])

    data = {
        'message': m,
    }
    if request.method == 'GET':
        return HttpResponse(json.dumps(data), content_type="application/json")

    elif request.method == 'POST':
        return HttpResponse(json.dumps(data), content_type="application/json")


@csrf_exempt
def returnData(request):
    info = db_show
    print(info)
    data = {
        'name': 'Alex-LC-Qiu',
        'age': 21,
    }
    if request.method == 'GET':
        return HttpResponse(json.dumps(data), content_type="application/json")

    elif request.method == 'POST':
        return HttpResponse(json.dumps(data), content_type="application/json")
