from django.db import models

# Create your models here.


class psn(models.Model):
    psnid = models.CharField(max_length=64, primary_key=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    # question = models.CharField(max_length=20)
    # answer = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    tel = models.CharField(max_length=15)


class psn_resume(models.Model):
    psnid = models.ForeignKey(
        'psn', on_delete=models.CASCADE)
    resumeid = models.CharField(max_length=64, primary_key=True)
    email = models.CharField(max_length=30, default='example@example.com')
    tel = models.CharField(max_length=15, default='13755555555')
    name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    sex = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    jobAdd = models.CharField(max_length=20)
    jobName = models.CharField(max_length=30)
    jobType = models.CharField(max_length=10)
    jobPay = models.CharField(max_length=12)
    nowStatus = models.CharField(max_length=2, default='0')
    updateTime = models.DateField(auto_now=True)
    workExp = models.CharField(max_length=15, default='应届')
    selfDisp = models.TextField(default='请输入一段自我描述')
    psnTag = models.TextField(default='个人能力,执行力')
    degree = models.CharField(max_length=10)


class psn_resume_project_exprience(models.Model):
    projectid = models.CharField(max_length=64, primary_key=True)
    resumeid = models.ForeignKey(
        'psn_resume', on_delete=models.CASCADE)
    projectName = models.CharField(max_length=30)
    jobName = models.CharField(max_length=30)
    orgName = models.CharField(max_length=50)
    startTime = models.DateField(auto_now=False, auto_now_add=False)
    endTime = models.DateField(auto_now=False, auto_now_add=False)
    tecName = models.CharField(max_length=30)
    projectDisp = models.TextField()


class psn_resume_work_exprience(models.Model):
    workid = models.CharField(max_length=64, primary_key=True)
    resumeid = models.ForeignKey(
        'psn_resume', on_delete=models.CASCADE)
    jobName = models.CharField(max_length=30)
    companyName = models.CharField(max_length=50)
    startTime = models.DateField(auto_now=False, auto_now_add=False)
    endTime = models.DateField(auto_now=False, auto_now_add=False)
    workDisp = models.TextField()


class psn_resume_edu_exprience(models.Model):
    eduid = models.CharField(max_length=64, primary_key=True)
    resumeid = models.ForeignKey(
        'psn_resume', on_delete=models.CASCADE)
    majorName = models.CharField(max_length=30)
    schoolName = models.CharField(max_length=50)
    gradTime = models.IntegerField(default=2019)
    degree = models.CharField(max_length=10)


class send_job(models.Model):
    resumeid = models.ForeignKey(
        'psn_resume', on_delete=models.CASCADE)
    psnid = models.ForeignKey(
        'psn', on_delete=models.CASCADE)
    entid = models.ForeignKey(
        'ent', on_delete=models.CASCADE)
    jobid = models.ForeignKey(
        'ent_jobs', on_delete=models.CASCADE)
    entName = models.CharField(max_length=50)
    jobName = models.CharField(max_length=20)
    status = models.CharField(max_length=10, default='已送达')
    sendTime = models.DateField(auto_now=True)
    wantJobName = models.CharField(max_length=20)
    wantJobPay = models.CharField(max_length=12)
    wantJobAdd = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    psnemail = models.CharField(max_length=30)
    psntel = models.CharField(max_length=15)
    entemail = models.CharField(max_length=30)
    enttel = models.CharField(max_length=15)


class ent(models.Model):
    entid = models.CharField(max_length=64, primary_key=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    # question = models.CharField(max_length=20)
    # answer = models.CharField(max_length=20)
    tel = models.CharField(max_length=15)
    email = models.CharField(max_length=30)


class ent_baseInfo(models.Model):
    entid = models.ForeignKey(
        'ent', on_delete=models.CASCADE)
    entAddress = models.CharField(max_length=20)
    entName = models.CharField(max_length=50)
    entContectName = models.CharField(max_length=20, default='HR')
    entCertId = models.CharField(max_length=20)
    entClass = models.CharField(max_length=20, default='私营企业')
    entScale = models.CharField(max_length=20, default='1-49人')
    entSummary = models.TextField()
    entTag = models.TextField(default='五险一金')


class ent_jobs(models.Model):
    entid = models.ForeignKey(
        'ent', on_delete=models.CASCADE)
    entName = models.CharField(max_length=50)
    entTag = models.TextField()
    jobid = models.CharField(max_length=64, primary_key=True)
    jobName = models.CharField(max_length=20)
    jobAddress = models.CharField(max_length=50)
    jobPay = models.CharField(max_length=30, default='面议')
    jobType = models.CharField(max_length=10, default='全职')
    jobClass = models.CharField(max_length=50)
    jobDepart = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    degree = models.CharField(max_length=10, default='不限')
    workExp = models.CharField(max_length=15, default='不限')
    jobReq = models.TextField()
    updateTime = models.DateField(auto_now=True)
