from .models import polls_model

# 数据库操作


def insert(name, age, sex, tel):
    test1 = polls_model(name=name, age=age, sex=sex, tel=tel)
    test1.save()
    # return HttpResponse('<p>数据添加成功！</p>')
    return 1


def show(name):
    response = '',
    list = polls_model.objects.filter(name=name).order_by("id")
    for value in list:
        response = value.name

    # return HttpResponse('<p>'+response+'<p>')
    return response
