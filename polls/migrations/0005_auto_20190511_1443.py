# Generated by Django 2.1.4 on 2019-05-11 06:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20190511_1443'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ent_baseinfo',
            old_name='entIntroduction',
            new_name='entSummary',
        ),
    ]