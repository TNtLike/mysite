# Generated by Django 2.1.4 on 2019-05-11 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ent_baseinfo',
            name='entContectName',
            field=models.CharField(default='testname', max_length=20),
        ),
    ]