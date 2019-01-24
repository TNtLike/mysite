# Generated by Django 2.1.4 on 2019-01-24 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='enterprise',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('question', models.CharField(max_length=20)),
                ('answer', models.CharField(max_length=20)),
                ('enterpriseemail', models.CharField(max_length=20)),
                ('enterpriseName', models.CharField(max_length=50)),
                ('enterpriseNumber', models.CharField(max_length=50)),
                ('enterpriseIntroduction', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='enterprise_jobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enterpriseName', models.CharField(max_length=50)),
                ('jobsName', models.CharField(max_length=20)),
                ('jobsCodition', models.CharField(max_length=30)),
                ('jobsLocation', models.CharField(max_length=30)),
                ('jobsPay', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='person_resume',
            fields=[
                ('relName', models.AutoField(primary_key=True, serialize=False)),
                ('gender', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=20)),
                ('nowJobs', models.CharField(max_length=20)),
                ('nowPay', models.CharField(max_length=20)),
                ('personIntroduction', models.TextField()),
            ],
        ),
        migrations.RenameModel(
            old_name='user',
            new_name='person',
        ),
        migrations.DeleteModel(
            name='polls_model',
        ),
    ]
