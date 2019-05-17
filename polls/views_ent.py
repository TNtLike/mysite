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
from .models import ent
from .models import ent_jobs
from .models import ent_baseInfo


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
            msg = '邮箱已被注册，请更换'
        elif ent.objects.get(tel=message['tel']):
            status = 'error'
            msg = '手机号已被注册，请更换'
    except ent.DoesNotExist:
        saveNewEntId = str(uuid.uuid1())
        saveNewEnt = ent(entid=saveNewEntId, username=message['username'], password=message['password'],
                         question=message['question'], answer=message['answer'], email=message['email'], tel=message['tel'])
        if saveNewEnt.save():
            status = 'error'
            msg = '注册失败'
        else:
            request.session['entid'] = saveNewEntId
            status = 'ok'
            msg = saveNewEntId
    data = {
        'status': status,
        'msg': msg
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


# 企业保存基本信息
@csrf_exempt
def subEntBaseInfo(request):
    message = json.loads(request.body)
    status = 'error'
    msg = ''
    if request.session.get('entid'):
        try:
            if ent_baseInfo.objects.get(entName=message['entName']):
                status = 'error'
                msg = '企业名已存在，请更换'
            elif ent_baseInfo.objects.get(entCertId=message['email']):
                status = 'error'
                msg = '营业执照已被占用，请确认'
        except ent_baseInfo.DoesNotExist:
            # saveNewEntId = str(uuid.uuid1())
            saveNewEntBaseInfo = ent_baseInfo(entid_id=request.session.get('entid'),
                                              entName=message['entName'], entContectName=message['entContectName'],
                                              entAddress=message['entAddress'], entCertId=message['entCertId'], entClass=message['entClass'], entScale=message['entScale'], entSummary=message['entSummary'])
            if saveNewEntBaseInfo.save():
                status = 'error'
                msg = '保存失败'
            else:
                # request.session['entid'] = saveNewEntId
                status = 'ok'
                msg = ''
    else:
        status = "error"
        msg = '登录超时，请重新登陆'

    data = {
        'status': status,
        'msg': msg
    }
    return HttpResponse(json.dumps(data), content_type="application/json")


# 企业提交职位信息
@csrf_exempt
def subEntJobInfo(request):
    message = json.loads(request.body)
    status = 'error'
    msg = ''
    if request.session.get('entid'):
        m = message['msg']
        key = message['key']
        if key != '0000':
            try:
                updateEntJobInfo = ent_jobs.objects.filter(
                    jobid=key).update(jobName=m['jobName'], jobDepart=m['jobDepart'], jobClass=m['jobClass'], jobType=m['jobType'], jobPay=m['jobPay'], jobLocation=m['jobLocation'], jobAddress=m['jobAddress'], workExp=m['workExp'], degree=m['degree'], jobReq=m['jobReq'], email=m['email'], updateTime=datetime.date.today())
                if updateEntJobInfo:
                    status = 'ok'
                    msg = '保存成功'
                else:
                    msg = '保存失败'
            except ent_jobs.DoesNotExist:
                msg = '简历信息不存在'
        else:
            saveNewJobInfoId = str(uuid.uuid1())
            saveNewJobInfo = ent_jobs(jobid=saveNewJobInfoId, entid_id=message['entid'], jobName=m['jobName'], jobDepart=m['jobDepart'], jobClass=m['jobClass'], jobType=m['jobType'], jobPay=m[
                                      'jobPay'], jobLocation=m['jobLocation'], jobAddress=m['jobAddress'], workExp=m['workExp'], degree=m['degree'], jobReq=m['jobReq'], email=m['email'], updateTime=datetime.date.today())
            if saveNewJobInfo.save():
                msg = '添加失败'
            else:
                status = 'ok'
                msg = '添加成功'
    else:
        msg = '登陆超时，请重新登陆'
    data = {
        'status': status,
        'msg': msg,
    }
    return HttpResponse(json.dumps(data), content_type="application/json")
