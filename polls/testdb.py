from .models import polls_model
from django.http import HttpResponse, JsonResponse

# 数据库操作


def insert(title, author, context):
    test1 = polls_model(title=title, author=author, context=context)
    test1.save()
    # return HttpResponse('<p>数据添加成功！</p>')
    return 1


def show():
    list = polls_model.objects.filter().order_by("id")
    for value in list:
        response = value.name

    # return HttpResponse('<p>'+response+'<p>')
    # return HttpResponse(list)
    return list
