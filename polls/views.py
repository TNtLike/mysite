from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import datetime
import json
from .models import polls_model


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def polls(request):
    return HttpResponse("Hello, Django. My name is Alex Qiu.")


def home_page(request):
    context = {}
    context['message'] = '{}'.format(datetime.datetime.now())
    return render(request, 'hello.html', context)


@csrf_exempt
def testVue(request):
    response = '',
    list = polls_model.objects.filter(name="Alex-LC-Qiu").order_by("id")
    for value in list:
        response = value.name

    data = {
        'name': response,
        'age': 21,
    }
    if request.method == 'GET':
        return HttpResponse(json.dumps(data), content_type="application/json")

    elif request.method == 'POST':
        return HttpResponse(json.dumps(data), content_type="application/json")
