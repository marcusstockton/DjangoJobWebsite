# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-31 02:01
from __future__ import unicode_literals

import Attachment.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Attachment', '0002_attachment_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attachment',
            name='active',
        ),
        migrations.RemoveField(
            model_name='attachment',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='attachment',
            name='data',
        ),
        migrations.RemoveField(
            model_name='attachment',
            name='file_name',
        ),
        migrations.RemoveField(
            model_name='attachment',
            name='file_type',
        ),
        migrations.AddField(
            model_name='attachment',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to=Attachment.models.upload_location),
        ),
        migrations.AddField(
            model_name='attachment',
            name='cv',
            field=models.FileField(blank=True, upload_to=Attachment.models.upload_location),
        ),
    ]