# Generated by Django 2.1.4 on 2019-05-14 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_auto_20190514_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='psn_resume',
            name='jobPay',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='psn_resume',
            name='jobType',
            field=models.CharField(max_length=10),
        ),
    ]