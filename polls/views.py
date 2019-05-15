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

# model
from .models import psn
from .models import psn_resume
from .models import ent
from .models import ent_jobs
from .models import ent_baseInfo
from .models import psn_resume_project_exprience
from .models import psn_resume_work_exprience
from .models import psn_resume_edu_exprience


# 登出 删除会话
@csrf_exempt
def loginOut(request):
    status = 'ok'
    msg = '退出成功'
    if request.session.get('entid'):
        try:
            del request.session['entid']
        except KeyError:
            status = 'error'
            msg = '退出失败，请重试'
    elif request.session.get('psnid'):
        try:
            del request.session['psnid']
        except KeyError:
            status = 'error'
            msg = '退出失败，请重试'
    data = {
        'status': status,
        'msg': msg
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
