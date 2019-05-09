from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

import datetime
import json
# 生成id
import uuid
from django.core import serializers

# email
from django.core.mail import EmailMessage

from .models import psn
from .models import psn_resume
from .models import ent
from .models import ent_jobs
from .models import ent_baseInfo


# 个人用户注册
@csrf_exempt
def psnSubmitUser(request):
    message = json.loads(request.body)
    try:
        if psn.objects.get(username=message['username']):
            status = 'error'
            msg = '用户名已存在，请更换'
        elif psn.objects.get(email=message['email']):
            status = 'error'
            msg = '邮箱已被占用，请更换'
    except psn.DoesNotExist:
        save_new_psn_psnid = str(uuid.uuid1())
        save_new_psn = psn(psnid=save_new_psn_psnid, username=message['username'], password=message['password'],
                           question=message['question'], answer=message['answer'], email=message['email'], tel=message['tel'])
        if save_new_psn.save():
            status = 'error'
            msg = '注册失败'
        else:
            request.session['psnid'] = save_new_psn_psnid
            status = 'ok'
            msg = save_new_psn_psnid
    data = {
        'status': status,
        'msg': msg
    }
    return HttpResponse(json.dumps(data), content_type="application/json")


# 企业用户注册
@csrf_exempt
def entSubmitUser(request):
    message = json.loads(request.body)
    try:
        if ent.objects.get(username=message['username']):
            status = 'error'
            msg = '用户名已存在，请更换'
        elif ent.objects.get(email=message['email']):
            status = 'error'
            msg = '邮箱已被占用，请更换'
    except ent.DoesNotExist:
        save_new_ent_entid = str(uuid.uuid1())
        save_new_ent = ent(entid=save_new_ent_entid, username=message['username'], password=message['password'],
                           question=message['question'], answer=message['answer'], email=message['email'], tel=message['tel'])
        if save_new_ent.save():
            status = 'error'
            msg = '注册失败'
        else:
            request.session['entid'] = save_new_ent_entid
            status = 'ok'
            msg = save_new_ent_entid
    data = {
        'status': status,
        'msg': msg
    }
    return HttpResponse(json.dumps(data), content_type="application/json")


# 个人登录
@csrf_exempt
def psnLogin(request):
    message = json.loads(request.body)
    status = 0
    msg = ''
    try:
        m = psn.objects.get(username=message['username'])
        if m.password == message['password']:
            request.session['psnid'] = m.psnid
            status = 1
            status = m.psnid
    except psn.DoesNotExist:
        status = 2
        status = ''
    data = {
        'status': status,
        'mag': msg
        # 'username': username
    }
    return HttpResponse(json.dumps(data), content_type="application/json")


# 企业登录
@csrf_exempt
def entLogin(request):
    message = json.loads(request.body)
    status = 0
    msg = ''
    try:
        m = ent.objects.get(username=message['username'])
        if m.password == message['password']:
            request.session['entid'] = m.entid
            status = 1
            msg = m.entid
    except ent.DoesNotExist:
        status = 2
        msg = ''
    data = {
        'status': status,
        'msg': msg
        # 'username': username
    }
    return HttpResponse(json.dumps(data), content_type="application/json")


# 发送邮件测试
@csrf_exempt
def sendEmail(resHostList, code):
    title = u'邮件主题'
    host = 'qiulangcheng@qlcnb.club'
    resHost = resHostList
    html_content = "<h2>您好！</h2> <p>欢迎注册，验证码为：" + code + "。</p> <p>如非本人注册请忽略此邮件</p>"
    email = EmailMessage(title, html_content, host, resHost)
    email.content_subtype = "html"
    if email.send():
        return "ok"
    else:
        return "error"
