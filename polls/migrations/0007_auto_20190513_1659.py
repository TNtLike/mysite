# Generated by Django 2.1.4 on 2019-05-13 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20190511_1445'),
    ]

    operations = [
        migrations.AddField(
            model_name='psn_resume',
            name='email',
            field=models.CharField(default='example@example.com', max_length=30),
        ),
        migrations.AddField(
            model_name='psn_resume',
            name='tel',
            field=models.CharField(default='13755555555', max_length=15),
        ),
    ]