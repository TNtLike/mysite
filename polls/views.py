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
            msg = '邮箱已被注册，请更换'
        elif psn.objects.get(tel=message['tel']):
            status = 'error'
            msg = '邮箱已被注册，请更换'
    except psn.DoesNotExist:
        saveNewPsnId = str(uuid.uuid1())
        saveNewPsn = psn(psnid=saveNewPsnId, username=message['username'], password=message['password'],
                         question=message['question'], answer=message['answer'], email=message['email'], tel=message['tel'])
        if saveNewPsn.save():
            status = 'error'
            msg = '注册失败'
        else:
               # 注册个人用户的同时创建一份简历
            saveNewPsnResumeId = str(uuid.uuid1())
            saveNewPsnResume = psn_resume(
                resumeid=saveNewPsnResumeId, psnid_id=saveNewPsnId, email=message['email'], tel=message['tel'])
            saveNewPsnResume.save()
            request.session['psnid'] = saveNewPsnId
            status = 'ok'
            msg = saveNewPsnId
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
            msg = m.psnid
    except psn.DoesNotExist:
        status = 2
        msg = ''
    data = {
        'status': status,
        'msg': msg
        # 'username': username
    }
    return HttpResponse(json.dumps(data), content_type="application/json")


# 查询简历信息
@csrf_exempt
def getPsnResumeInfo(request):
    message = json.loads(request.body)
    status = 'error'
    msg = ''
    if request.session.get('psnid'):
        try:
            m = psn_resume.objects.filter(psnid_id=message['psnid'])
            status = 'ok'
            msg = serializers.serialize('json', m)
        except psn_resume.DoesNotExist:
            msg = '简历信息不存在'
    else:
        msg = '登陆超时，请重新登陆'
    data = {
        'status': status,
        'msg': msg
    }
    return HttpResponse(json.dumps(data), content_type="application/json")


# 保存个人基本信息
@csrf_exempt
def subPsnBaseInfo(request):
    message = json.loads(request.body)
    status = 'error'
    msg = ''
    if request.session.get('psnid'):
        m = message['msg']
        try:
            updatePsnBaseInfo = psn_resume.objects.filter(
                psnid_id=message['psnid']).update(name=m['name'], age=m['age'], sex=m['sex'], location=m['location'], jobName=m['jobName'], jobPay=m['jobPay'], jobType=m['jobType'], jobAdd=m['jobAdd'], tel=m['tel'], email=m['email'], nowStatus=m['nowStatus'], updateTime=datetime.date.today())
            if updatePsnBaseInfo:
                status = 'ok'
                msg = '保存成功'
            else:
                msg = '保存失败'
        except psn_resume.DoesNotExist:
            msg = '简历信息不存在'
    else:
        msg = '登陆超时，请重新登陆'
    data = {
        'status': status,
        'msg': msg
    }
    return HttpResponse(json.dumps(data), content_type="application/json")


# 保存个人项目信息
@csrf_exempt
def subPsnProjectInfo(request):
    message = json.loads(request.body)
    status = 'error'
    msg = ''
    if request.session.get('psnid'):
        m = message['msg']
        key = message['key']
        resumeid = psn_resume.objects.get(
            psnid_id=message['psnid']).resumeid
        if key != '0000':
            try:
                updatePsnBaseInfo = psn_resume_project_exprience.objects.filter(
                    resumeid_id=resumeid).update(jobName=m['jobName'], orgName=m['orgName'], startTime=m['startTime'], endTime=m['endTime'], tecName=m['tecName'], projectDisp=m['projectDisp'])
                if updatePsnBaseInfo:
                    status = 'ok'
                    msg = '保存成功'
                else:
                    msg = '保存失败'
            except psn_resume_project_exprience.DoesNotExist:
                msg = '简历信息不存在'
        else:
            saveNewProjectInfoId = str(uuid.uuid1())
            saveNewProjectInfo = psn_resume_project_exprience(projectid=saveNewProjectInfoId, resumeid_id=resumeid, jobName=m['jobName'], orgName=m[
                                                              'orgName'], startTime=m['startTime'], endTime=m['endTime'], tecName=m['tecName'], projectDisp=m['projectDisp'])
            if saveNewProjectInfo.save():
                msg = '添加失败'
            else:
                status = 'ok'
                msg = serializers.serialize('json', psn_resume_project_exprience.objects.filter(
                    resumeid_id=resumeid))
    else:
        msg = '登陆超时，请重新登陆'
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


# 企业提交基本信息
@csrf_exempt
def entBaseInfoSub(request):
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
