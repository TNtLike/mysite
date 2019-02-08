from django.db import models

# Create your models here.


class person(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    question = models.CharField(max_length=20)
    answer = models.CharField(max_length=20)
    email = models.CharField(max_length=20)


class person_resume(models.Model):
    relName = models.AutoField(primary_key=True)
    gender = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    nowJobs = models.CharField(max_length=20)
    nowPay = models.CharField(max_length=20)
    personIntroduction = models.TextField()


class person_baseInfo(models.Model):
    name = models.CharField(max_length=20)
    sex = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    industry = models.CharField(max_length=20)
    function = models.CharField(max_length=20)
    position = models.CharField(max_length=20)
    companyName = models.CharField(max_length=20)
    startWork = models.CharField(max_length=20)


class enterprise(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    question = models.CharField(max_length=20)
    answer = models.CharField(max_length=20)
    enterpriseemail = models.CharField(max_length=20)
    enterpriseName = models.CharField(max_length=50)
    enterpriseNumber = models.CharField(max_length=50)
    enterpriseIntroduction = models.TextField()


class enterprise_jobs(models.Model):
    enterpriseName = models.CharField(max_length=50)
    jobsName = models.CharField(max_length=20)
    jobsCodition = models.CharField(max_length=30)
    jobsLocation = models.CharField(max_length=30)
    jobsPay = models.CharField(max_length=30)
