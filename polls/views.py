from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def polls(request):
    return HttpResponse("Hello, Django. My name is Alex Qiu.")


def home_page(request):
    context = {}
    context['context'] = 'hello qlc'
    return render(request, 'hello.html', context)
