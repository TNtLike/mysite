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
from .models import psn_resume_project_exprience
from .models import psn_resume_work_exprience
from .models import psn_resume_edu_exprience


# 个人用户注册
@csrf_exempt
def psnSubmitUser(request):
    message = json.loads(request.body)
    # if psn.objects.get(username=message['username']) or psn.objects.get(email=message['email']) or psn.objects.get(tel=message['tel']):

    if psn.objects.filter(username=message['username']):
        status = 'error'
        msg = '用户名已存在，请更换'
    elif psn.objects.filter(email=message['email']):
        status = 'error'
        msg = '邮箱已被注册，请更换'
    elif psn.objects.filter(tel=message['tel']):
        status = 'error'
        msg = '手机已被注册，请更换'
    else:
        saveNewPsnId = str(uuid.uuid1())
        # saveNewPsn = psn(psnid=saveNewPsnId, username=message['username'], password=message['password'],
        #                  question=message['question'], answer=message['answer'], email=message['email'], tel=message['tel'])
        saveNewPsn = psn(psnid=saveNewPsnId, username=message['username'], password=message['password'],
                         email=message['email'], tel=message['tel'])
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
    data = {
    }
    if request.session.get('psnid'):
        try:
            resumeid = psn_resume.objects.filter(
                psnid_id=message['psnid'])[0].resumeid
            status = 'ok'
            data['psnBaseInfo'] = serializers.serialize(
                'json', psn_resume.objects.order_by(
                    "updateTime").filter(psnid_id=message['psnid']))
            data['psnProjectInfo'] = serializers.serialize(
                'json', psn_resume_project_exprience.objects.order_by(
                    "startTime").filter(
                    resumeid_id=resumeid))
            data['psnWorkInfo'] = serializers.serialize(
                'json', psn_resume_work_exprience.objects.order_by(
                    "startTime").filter(
                    resumeid_id=resumeid))
            data['psnEduInfo'] = serializers.serialize(
                'json', psn_resume_edu_exprience.objects.order_by(
                    "gradTime").filter(
                    resumeid_id=resumeid))
        except psn_resume.DoesNotExist:
            msg = '简历信息不存在'
    else:
        msg = '登陆超时，请重新登陆'
    data = {
        'status': status,
        'msg': msg,
        'data': data
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
                psnid_id=message['psnid']).update(name=m['name'], age=m['age'], sex=m['sex'], location=m['location'], workExp=m['workExp'], jobName=m['jobName'], jobPay=m['jobPay'], jobType=m['jobType'], jobAdd=m['jobAdd'], tel=m['tel'], email=m['email'], nowStatus=m['nowStatus'], selfDisp=m['selfDisp'], psnTag=m['psnTag'], degree=m['degree'], updateTime=datetime.date.today())
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
    data = {}
    if request.session.get('psnid'):
        m = message['msg']
        key = message['key']
        resumeid = psn_resume.objects.filter(
            psnid_id=message['psnid'])[0].resumeid
        if key != '0000':
            try:
                updatePsnProjectInfo = psn_resume_project_exprience.objects.filter(
                    projectid=key).update(projectName=m['projectName'], jobName=m['jobName'], orgName=m['orgName'], startTime=m['startTime'], endTime=m['endTime'], tecName=m['tecName'], projectDisp=m['projectDisp'])
                if updatePsnProjectInfo:
                    status = 'ok'
                    msg = '保存成功'
                    data = serializers.serialize('json', psn_resume_project_exprience.objects.order_by(
                        "startTime").filter(
                        resumeid_id=resumeid))
                else:
                    msg = '保存失败'
            except psn_resume_project_exprience.DoesNotExist:
                msg = '简历信息不存在'
        else:
            saveNewProjectInfoId = str(uuid.uuid1())
            saveNewProjectInfo = psn_resume_project_exprience(projectid=saveNewProjectInfoId, resumeid_id=resumeid, projectName=m['projectName'], jobName=m['jobName'], orgName=m[
                'orgName'], startTime=m['startTime'], endTime=m['endTime'], tecName=m['tecName'], projectDisp=m['projectDisp'])
            if saveNewProjectInfo.save():
                msg = '添加失败'
            else:
                status = 'ok'
                msg = '添加成功'
                data = serializers.serialize('json', psn_resume_project_exprience.objects.order_by(
                    "startTime").filter(
                    resumeid_id=resumeid))
    else:
        msg = '登陆超时，请重新登陆'
    data = {
        'status': status,
        'msg': msg,
        'data': data
    }
    return HttpResponse(json.dumps(data), content_type="application/json")


# 删除项目信息
@csrf_exempt
def delPsnProjectInfo(request):
    message = json.loads(request.body)
    status = 'error'
    msg = ''
    if request.session.get('psnid'):
        try:
            m = psn_resume_project_exprience.objects.get(
                projectid=message['msg'])
            print(m.delete())
            status = 'ok'
            msg = '删除成功'
        except psn_resume_project_exprience.DoesNotExist:
            msg = '删除失败'
    else:
        msg = '登陆超时'
    data = {
        'status': status,
        'msg': msg,
    }
    return HttpResponse(json.dumps(data), content_type="application/json")


# 保存工作经历信息
@csrf_exempt
def subPsnWorkInfo(request):
    message = json.loads(request.body)
    status = 'error'
    msg = ''
    data = {}
    if request.session.get('psnid'):
        m = message['msg']
        key = message['key']
        resumeid = psn_resume.objects.filter(
            psnid_id=message['psnid'])[0].resumeid
        if key != '0000':
            try:
                updatePsnWorkInfo = psn_resume_work_exprience.objects.filter(
                    workid=key).update(companyName=m['companyName'], jobName=m['jobName'], startTime=m['startTime'], endTime=m['endTime'], workDisp=m['workDisp'])
                if updatePsnWorkInfo:
                    status = 'ok'
                    msg = '保存成功'
                    data = serializers.serialize('json', psn_resume_work_exprience.objects.order_by(
                        "startTime").filter(
                        resumeid_id=resumeid))
                else:
                    msg = '保存失败'
            except psn_resume_work_exprience.DoesNotExist:
                msg = '简历信息不存在'
        else:
            saveNewWorkInfoId = str(uuid.uuid1())
            saveNewWorkInfo = psn_resume_work_exprience(workid=saveNewWorkInfoId, resumeid_id=resumeid, jobName=m['jobName'], companyName=m[
                'companyName'], startTime=m['startTime'], endTime=m['endTime'], workDisp=m['workDisp'])
            if saveNewWorkInfo.save():
                msg = '添加失败'
            else:
                status = 'ok'
                msg = '添加成功'
                data = serializers.serialize('json', psn_resume_work_exprience.objects.order_by(
                    "startTime").filter(
                    resumeid_id=resumeid))
    else:
        msg = '登陆超时，请重新登陆'
    data = {
        'status': status,
        'msg': msg,
        'data': data
    }
    return HttpResponse(json.dumps(data), content_type="application/json")


# 删除工作经历信息
@csrf_exempt
def delPsnWorkInfo(request):
    message = json.loads(request.body)
    status = 'error'
    msg = ''
    if request.session.get('psnid'):
        try:
            m = psn_resume_work_exprience.objects.get(
                workid=message['msg'])
            print(m.delete())
            status = 'ok'
            msg = '删除成功'
        except psn_resume_work_exprience.DoesNotExist:
            msg = '删除失败'
    else:
        msg = '登陆超时'
    data = {
        'status': status,
        'msg': msg,
    }
    return HttpResponse(json.dumps(data), content_type="application/json")


# 保存教育经历信息
@csrf_exempt
def subPsnEduInfo(request):
    message = json.loads(request.body)
    status = 'error'
    msg = ''
    data = {}
    if request.session.get('psnid'):
        m = message['msg']
        key = message['key']
        resumeid = psn_resume.objects.filter(
            psnid_id=message['psnid'])[0].resumeid
        if key != '0000':
            try:
                updatePsnEduInfo = psn_resume_edu_exprience.objects.filter(
                    eduid=key).update(schoolName=m['schoolName'], majorName=m['majorName'], gradTime=m['gradTime'], degree=m['degree'])
                if updatePsnEduInfo:
                    status = 'ok'
                    msg = '保存成功'
                    data = serializers.serialize('json', psn_resume_edu_exprience.objects.order_by(
                        "gradTime").filter(
                        resumeid_id=resumeid))
                else:
                    msg = '保存失败'
            except psn_resume_edu_exprience.DoesNotExist:
                msg = '简历信息不存在'
        else:
            saveNewEduInfoId = str(uuid.uuid1())
            saveNewEduInfo = psn_resume_edu_exprience(eduid=saveNewEduInfoId, resumeid_id=resumeid, majorName=m['majorName'], schoolName=m[
                'schoolName'], gradTime=m['gradTime'], degree=m['degree'])
            if saveNewEduInfo.save():
                msg = '添加失败'
            else:
                status = 'ok'
                msg = '添加成功'
                data = serializers.serialize('json', psn_resume_edu_exprience.objects.order_by(
                    "gradTime").filter(
                    resumeid_id=resumeid))
    else:
        msg = '登陆超时，请重新登陆'
    data = {
        'status': status,
        'msg': msg,
        'data': data
    }
    return HttpResponse(json.dumps(data), content_type="application/json")


# 删除教育经历信息
@csrf_exempt
def delPsnEduInfo(request):
    message = json.loads(request.body)
    status = 'error'
    msg = ''
    if request.session.get('psnid'):
        try:
            m = psn_resume_edu_exprience.objects.get(
                eduid=message['msg'])
            print(m.delete())
            status = 'ok'
            msg = '删除成功'
        except psn_resume_edu_exprience.DoesNotExist:
            msg = '删除失败'
    else:
        msg = '登陆超时'
    data = {
        'status': status,
        'msg': msg,
    }
    return HttpResponse(json.dumps(data), content_type="application/json")
