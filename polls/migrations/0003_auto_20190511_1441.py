# Generated by Django 2.1.4 on 2019-05-11 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_ent_baseinfo_entcontectname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ent_baseinfo',
            old_name='entLocation',
            new_name='entAddress',
        ),
        migrations.AlterField(
            model_name='ent_baseinfo',
            name='entContectName',
            field=models.CharField(default='entContectName', max_length=20),
        ),
    ]
