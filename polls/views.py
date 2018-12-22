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


def db_add(request):
    message = testdb.insert()
    return HttpResponse('<p>'+message+'<p>')


def db_show(request):
    response = testdb.show()
    return HttpResponse('<p>'+response+'<p>')


@csrf_exempt
def getData(request):
    return 0


@csrf_exempt
def returnData(request):
    data = {
        'name': 'Alex-LC-Qiu',
        'age': 21,
    }
    if request.method == 'GET':
        return HttpResponse(json.dumps(data), content_type="application/json")

    elif request.method == 'POST':
        return HttpResponse(json.dumps(data), content_type="application/json")
