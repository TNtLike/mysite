# Generated by Django 2.1.4 on 2019-05-17 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0017_psn_resume_selfdisp'),
    ]

    operations = [
        migrations.AddField(
            model_name='psn_resume',
            name='workExp',
            field=models.CharField(default='实习生', max_length=15),
        ),
    ]
