from django.db import models

# Create your models here.


class user(models.Model):
    id = models.AutoField(primary_key=True)
    password = models.CharField(max_length=20)
    is_superuser = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=20)


class polls_model(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20)
    author = models.CharField(max_length=20)
    content = models.TextField()
    type = models.CharField(max_length=20)


class polls_model(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20)
    author = models.CharField(max_length=20)
    content = models.TextField()
    type = models.CharField(max_length=20)
