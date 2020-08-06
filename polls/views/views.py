from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
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
from .models import send_job


# 设置首页index.html
@csrf_exempt
def returnIndex(request):
    return render(request, 'index.html')


# 查询账号信息
@csrf_exempt
def getAccountInfo(request):
    message = json.loads(request.body)
    status = 'error'
    msg = '',
    accid = message['id']
    type = message['type']
    if type == 'psn':
        status = 'ok'
        msg = serializers.serialize('json', psn.objects.filter(psnid=accid))
    elif type == 'ent':
        status = 'ok'
        msg = serializers.serialize('json', ent.objects.filter(entid=accid))
    data = {
        'status': status,
        'msg': msg
    }
    return HttpResponse(json.dumps(data), content_type="application/json")


# 修改账号信息
@csrf_exempt
def subAccountInfo(request):
    message = json.loads(request.body)
    status = 'error'
    msg = '',
    accid = message['id']
    # type = message['type']
    m = message['msg']
    # if type == 'psn':
    if psn.objects.get(username=m['username']).psnid != accid:
        msg = '用户名已存在，请更换'
    elif psn.objects.get(email=m['email']).psnid != accid:
        msg = '邮箱已被注册，请更换'
    elif psn.objects.get(tel=m['tel']).psnid != accid:
        msg = '手机已被注册，请更换'
    else:
        updateAcc = psn.objects.filter(
            psnid=accid).update(username=m['username'], tel=m['tel'], email=m['email'], password=m['password'])
        if updateAcc:
            status = 'ok'
            msg = '保存成功'
    # elif type == 'ent':
    #     updateAcc = ent.objects.filter(
    #         entid=accid).update(username=m['username'], tel=m['tel'], email=m['email'], password=m['password'])
    #     if updateAcc:
    #         status = 'ok'
    #         msg = '保存成功'
    data = {
        'status': status,
        'msg': msg
    }
    return HttpResponse(json.dumps(data), content_type="application/json")


# 简历投递
@csrf_exempt
def sendResume(request):
    message = json.loads(request.body)
    status = 'error'
    msg = '',
    type = message['type']
    if type == 'psnsend':
        psnid = message['psnid']
        jobid = message['jobid']
        if request.session.get('psnid'):
            psnemail = psn.objects.get(psnid=psnid).email
            psntel = psn.objects.get(psnid=psnid).tel
            resumeid = psn_resume.objects.filter(psnid_id=psnid)[0].resumeid
            entid = ent_jobs.objects.get(jobid=jobid).entid_id
            entemail = ent.objects.get(entid=entid).email
            enttel = ent.objects.get(entid=entid).tel
            jobName = ent_jobs.objects.get(jobid=jobid).jobName
            entName = ent_jobs.objects.get(jobid=jobid).entName
            name = psn_resume.objects.get(resumeid=resumeid).name
            wantJobPay = psn_resume.objects.get(resumeid=resumeid).jobPay
            wantJobName = psn_resume.objects.get(resumeid=resumeid).jobName
            wantJobAdd = psn_resume.objects.get(resumeid=resumeid).jobAdd
            if send_job.objects.filter(resumeid_id=resumeid, jobid=jobid):
                msg = '请勿重复投递'
            else:
                addNewRec = send_job(resumeid_id=resumeid,
                                     jobid_id=jobid, entid_id=entid, psnid_id=psnid, jobName=jobName, entName=entName, name=name, wantJobName=wantJobName, wantJobPay=wantJobPay, wantJobAdd=wantJobAdd, psnemail=psnemail, psntel=psntel, entemail=entemail, enttel=enttel, sendTime=datetime.date.today())
                if addNewRec.save():
                    msg = '投递失败'
                else:
                    status = 'ok'
                    msg = '投递成功'
        else:
            msg = '登陆超时，请重新登陆'
    elif type == 'entsend':
        psnid = message['psnid']
        entid = message['entid']
        jobid = message['jobid']
        resumeid = message['resumeid']
    data = {
        'status': status,
        'msg': msg
    }
    return HttpResponse(json.dumps(data), content_type="application/json")


# 查询已投递的职位
@csrf_exempt
def getSentJob(request):
    message = json.loads(request.body)
    status = 'error'
    msg = ''
    if message['psnid']:
        psnid = message['psnid']
        if request.session.get('psnid'):
            resumeid = psn_resume.objects.filter(psnid_id=psnid)[0].resumeid
            status = 'ok'
            msg = serializers.serialize(
                'json', send_job.objects.order_by(
                    "sendTime").filter(resumeid_id=resumeid))
        else:
            msg = '登陆超时，请重新登陆'
    elif message['entid']:
        entid = message['entid']
        if request.session.get('entid'):
            status = 'ok'
            msg = serializers.serialize(
                'json', send_job.objects.filter(entid_id=entid))

        else:
            msg = '登陆超时，请重新登陆'
    data = {
        'status': status,
        'msg': msg,
    }
    return HttpResponse(json.dumps(data), content_type="application/json")


# 通过投递
@csrf_exempt
def passSent(request):
    message = json.loads(request.body)
    status = 'error'
    msg = ''
    if request.session.get('psnid'):
        m = message['msg']
        jobid = m['jobid']
        resumeid = m['resumeid']
        entid = m['entid']
        psnid = m['psnid']
        res = send_job.objects.filter(
            entid_id=entid, psnid_id=psnid, resumeid_id=resumeid, jobid_id=jobid).update(status='个人已同意', sendTime=datetime.date.today())
        status = 'ok'
        msg = '已同意'
    elif request.session.get('entid'):
        m = message['msg']
        jobid = m['jobid']
        resumeid = m['resumeid']
        entid = m['entid']
        psnid = m['psnid']
        psnemail = psn.objects.get(psnid=psnid).email
        psntel = psn.objects.get(psnid=psnid).tel
        entemail = ent.objects.get(entid=entid).email
        enttel = ent.objects.get(entid=entid).tel
        jobName = ent_jobs.objects.get(jobid=jobid).jobName
        entName = ent_jobs.objects.get(jobid=jobid).entName
        name = psn_resume.objects.get(resumeid=resumeid).name
        wantJobPay = psn_resume.objects.get(resumeid=resumeid).jobPay
        wantJobName = psn_resume.objects.get(resumeid=resumeid).jobName
        wantJobAdd = psn_resume.objects.get(resumeid=resumeid).jobAdd
        conname = ent_baseInfo.objects.get(entid_id=entid).entContectName
        # res = send_job.objects.filter(
        #     entid_id=entid, psnid_id=psnid, resumeid_id=resumeid, jobid_id=jobid).update(status='面试邀请')

        res = send_job.objects.filter(
            entid_id=entid, psnid_id=psnid, resumeid_id=resumeid, jobid_id=jobid).update(status='面试邀请', sendTime=datetime.date.today())
        if res == 0:
            # 即不存在该信息
            res = send_job(resumeid_id=resumeid, jobid_id=jobid, entid_id=entid, psnid_id=psnid,
                           jobName=jobName, entName=entName, name=name, wantJobName=wantJobName, wantJobPay=wantJobPay,
                           wantJobAdd=wantJobAdd, psnemail=psnemail, psntel=psntel, entemail=entemail,
                           enttel=enttel, status='面试邀请', sendTime=datetime.date.today())
            if res.save():
                msg = '操作失败'
            else:
                status = 'ok'
                msg = '操作成功'
        else:
            status = 'ok'
            msg = '已发送'
        sendEmail(psnemail, entName, name,
                  jobName, conname, enttel, entemail)
    else:
        msg = '登陆超时，请重新登陆'
    data = {
        'status': status,
        'msg': msg,
    }
    return HttpResponse(json.dumps(data), content_type="application/json")


# 拒绝投递
@csrf_exempt
def closeSent(request):
    message = json.loads(request.body)
    status = 'error'
    msg = ''
    if request.session.get('psnid'):
        m = message['msg']
        jobid = m['jobid']
        resumeid = m['resumeid']
        entid = m['entid']
        psnid = m['psnid']
        res = send_job.objects.filter(
            entid_id=entid, psnid_id=psnid, resumeid_id=resumeid, jobid_id=jobid).update(status='个人已拒绝', sendTime=datetime.date.today())
        status = 'ok'
        msg = '已拒绝'
    elif request.session.get('entid'):
        m = message['msg']
        jobid = m['jobid']
        resumeid = m['resumeid']
        entid = m['entid']
        psnid = m['psnid']
        res = send_job.objects.filter(
            entid_id=entid, psnid_id=psnid, resumeid_id=resumeid, jobid_id=jobid).update(status='企业已拒绝', sendTime=datetime.date.today())
        status = 'ok'
        msg = '已拒绝'

    else:
        msg = '登陆超时，请重新登陆'
    data = {
        'status': status,
        'msg': msg,
    }
    return HttpResponse(json.dumps(data), content_type="application/json")


# 关闭投递
@csrf_exempt
def delSent(request):
    message = json.loads(request.body)
    status = 'error'
    msg = ''
    if request.session.get('entid'):
        m = message['msg']
        jobid = m['jobid']
        resumeid = m['resumeid']
        entid = m['entid']
        psnid = m['psnid']
        res = send_job.objects.filter(
            entid_id=entid, psnid_id=psnid, resumeid_id=resumeid, jobid_id=jobid).update(status='订单已关闭', sendTime=datetime.date.today())
        status = 'ok'
        msg = '已关闭'
    else:
        msg = '登陆超时，请重新登陆'
    data = {
        'status': status,
        'msg': msg,
    }
    return HttpResponse(json.dumps(data), content_type="application/json")


# 个人用户查询职位
@csrf_exempt
def searchJob(request):
    message = json.loads(request.body)
    status = 'error'
    msg = {}
    key = message['key']  # key为jobid
    type = message['type']
    if key == '0000':
        if type == 'all':
                # 没有搜索条件则返回全部
            status = 'ok'
            res = ent_jobs.objects.all()
            msg = serializers.serialize(
                'json', res)
        else:
            # 如果有搜索条件
            m = message['msg']  # m 为搜索条件
            status = 'ok'
            res = ent_jobs.objects.all()
            if m['jobType']:
                res = res.filter(jobType=m['jobType'])
            if m['jobPay']:
                res = res.filter(jobPay=m['jobPay'])
            if m['workExp']:
                res = res.filter(workExp=m['workExp'])
            if m['degree']:
                res = res.filter(degree=m['degree'])
            if 'otherInfo' in m:
                res = res.filter(
                    Q(jobName__icontains=m['otherInfo']) | Q(entName__icontains=m['otherInfo']))
            msg = serializers.serialize('json', res)
    else:
        # 如果有jobid
        status = 'ok'
        msg['entJobInfo'] = serializers.serialize(
            'json', ent_jobs.objects.filter(
                jobid=key))
        entid = ent_jobs.objects.get(
            jobid=key).entid_id
        msg['entBaseInfo'] = serializers.serialize(
            'json', ent_baseInfo.objects.filter(
                entid_id=entid))
    data = {
        'status': status,
        'msg': msg
    }
    return HttpResponse(json.dumps(data), content_type="application/json")


# 企业用户用户查询个人
@csrf_exempt
def searchPsn(request):
    message = json.loads(request.body)
    status = 'error'
    msg = {}
    key = message['key']  # key为resumeid
    type = message['type']
    if key == '0000':
        if type == 'all':
                # 没有搜索条件则返回全部
            status = 'ok'
            res = psn_resume.objects.all()
            msg = serializers.serialize(
                'json', res)
        else:
            # 如果有搜索条件
            m = message['msg']  # m 为搜索条件
            res = psn_resume.objects.all()
            status = 'ok'
            if m['jobType']:
                res = res.filter(jobType=m['jobType'])
            if m['jobPay']:
                res = res.filter(jobPay=m['jobPay'])
            if m['workExp']:
                res = res.filter(workExp=m['workExp'])
            if m['degree']:
                res = res.filter(degree=m['degree'])
            if m['jobAdd']:
                res = res.filter(jobAdd=m['jobAdd'])
            if 'otherInfo' in m:
                res = res.filter(
                    Q(jobAdd__icontains=m['otherInfo']) | Q(jobName__icontains=m['otherInfo']))
            msg = serializers.serialize('json', res)
    else:
        # 如果有resumeid,返回完整的简历
        status = 'ok'
        msg['psnBaseInfo'] = serializers.serialize(
            'json', psn_resume.objects.order_by(
                "updateTime").filter(resumeid=key))
        msg['psnProjectInfo'] = serializers.serialize(
            'json', psn_resume_project_exprience.objects.order_by(
                "startTime").filter(
                resumeid_id=key))
        msg['psnWorkInfo'] = serializers.serialize(
            'json', psn_resume_work_exprience.objects.order_by(
                "startTime").filter(
                resumeid_id=key))
        msg['psnEduInfo'] = serializers.serialize(
            'json', psn_resume_edu_exprience.objects.order_by(
                "gradTime").filter(
                resumeid_id=key))
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
def sendEmail(psnemail, entname, name, jobname, conname, enttel, entemail):
    title = u'邮件主题'
    host = 'qiulangcheng@qlcnb.club'
    resHostList = []
    resHostList.append(psnemail)
    resHost = resHostList
    html_content = name+"<h2>您好！</h2> <p>企业：" + \
        entname + "。</p> <p>向您推荐了职位</p>"+jobname+'。<p>企业联系人：' + \
        conname+'</p><p>联系邮箱：'+entemail+'</p><p>联系电话：'+enttel+'</p>'
    email = EmailMessage(title, html_content, host, resHost)
    email.content_subtype = "html"
    if email.send():
        return "ok"
    else:
        return "error"
