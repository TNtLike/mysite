# Generated by Django 2.1.4 on 2019-05-17 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0018_psn_resume_workexp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='psn_resume',
            name='workExp',
            field=models.CharField(default='应届毕业生', max_length=15),
        ),
    ]