# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-10 15:52
from __future__ import unicode_literals

from django.db import migrations, models
import students.models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_auto_20160210_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='picture',
            field=models.FileField(upload_to=students.models.get_upload_file_name),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='picture',
            field=models.FileField(upload_to=students.models.get_upload_file_name),
        ),
    ]
