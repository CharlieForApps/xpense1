# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-07-16 15:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('period', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='period',
            name='enddate',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='period',
            name='startdate',
            field=models.DateTimeField(),
        ),
    ]
