from django.db import models

# Create your models here.


class polls_model(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    sex = models.CharField(max_length=10)
    tel = models.CharField(max_length=20)
