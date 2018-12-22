from django.http import HttpResponse

from .models import polls_model

# 数据库操作


def insert(request):
    test1 = polls_model(name='Alex-LC-Qiu')
    test1.save()
    return HttpResponse('<p>数据添加成功！</p>')


def show(request):
    response = '',
    list = polls_model.objects.filter(name="Alex-LC-Qiu").order_by("id")
    for value in list:
        response = value.name

    return HttpResponse('<p>'+response+'<p>')
