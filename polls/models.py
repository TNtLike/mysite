from django.db import models

# Create your models here.


class psn(models.Model):
    psnid = models.CharField(max_length=64, primary_key=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    question = models.CharField(max_length=20)
    answer = models.CharField(max_length=20)
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


class psn_resume_project_exprience(models.Model):
    projectid = models.CharField(max_length=64, primary_key=True)
    resumeid = models.ForeignKey(
        'psn_resume', on_delete=models.CASCADE)
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
    gradTime = models.DateField(auto_now=False, auto_now_add=False)
    degree = models.CharField(max_length=10)


class ent(models.Model):
    entid = models.CharField(max_length=64, primary_key=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    question = models.CharField(max_length=20)
    answer = models.CharField(max_length=20)
    tel = models.CharField(max_length=15)
    email = models.CharField(max_length=30)


class ent_baseInfo(models.Model):
    entid = models.ForeignKey(
        'ent', on_delete=models.CASCADE)
    entAddress = models.CharField(max_length=20)
    entName = models.CharField(max_length=20)
    entContectName = models.CharField(max_length=20, default='HR')
    entCertId = models.CharField(max_length=20)
    entClass = models.CharField(max_length=20, default='私营企业')
    entScale = models.CharField(max_length=20, default='1-49人')
    entSummary = models.TextField()


class ent_jobs(models.Model):
    entid = models.ForeignKey(
        'ent', on_delete=models.CASCADE)
    jobid = models.CharField(max_length=64, primary_key=True)
    enterpriseName = models.CharField(max_length=50)
    jobsName = models.CharField(max_length=20)
    jobsCodition = models.CharField(max_length=30)
    jobsLocation = models.CharField(max_length=30)
    jobsPay = models.CharField(max_length=30)
