# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2019-04-19 12:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_auto_20161122_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='file',
            field=models.FileField(upload_to='file/'),
        ),
    ]
