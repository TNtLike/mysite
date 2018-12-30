from django.db import models

# Create your models here.


class polls_model(models.Model):
    title = models.CharField(max_length=20)
    author = models.CharField(max_length=20)
    content = models.TextField()
    type = models.CharField(max_length=20)
