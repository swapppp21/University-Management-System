# Generated by Django 4.1.4 on 2022-12-19 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_teachermodel_teachesub'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teachermodel',
            name='mob',
        ),
        migrations.AddField(
            model_name='teachermodel',
            name='mobno',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
