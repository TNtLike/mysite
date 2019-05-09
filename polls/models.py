from django.db import models

# Create your models here.


class psn(models.Model):
    psnid = models.CharField(max_length=64, primary_key=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    question = models.CharField(max_length=20)
    answer = models.CharField(max_length=20)
    email = models.CharField(max_length=30)


class psn_resume(models.Model):
    resumeid = models.CharField(max_length=64, primary_key=True)
    gender = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    nowJobs = models.CharField(max_length=20)
    nowPay = models.CharField(max_length=20)
    personIntroduction = models.TextField()
    name = models.CharField(max_length=20)
    sex = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    industry = models.CharField(max_length=20)
    function = models.CharField(max_length=20)
    position = models.CharField(max_length=20)
    companyName = models.CharField(max_length=20)
    startWork = models.CharField(max_length=20)


class ent(models.Model):
    entid = models.CharField(max_length=64, primary_key=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    question = models.CharField(max_length=20)
    answer = models.CharField(max_length=20)


class ent_baseInfo(models.Model):
    entid = models.AutoField(max_length=64, primary_key=True)
    entLocation = models.CharField(max_length=20)
    entName = models.CharField(max_length=20)
    entEmail = models.CharField(max_length=20)
    entIntroduction = models.TextField()


class ent_jobs(models.Model):
    jobid = models.CharField(max_length=64, primary_key=True)
    enterpriseName = models.CharField(max_length=50)
    jobsName = models.CharField(max_length=20)
    jobsCodition = models.CharField(max_length=30)
    jobsLocation = models.CharField(max_length=30)
    jobsPay = models.CharField(max_length=30)
