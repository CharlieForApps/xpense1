# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-07-16 15:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0003_auto_20180715_2325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='cattype',
            field=models.CharField(choices=[('Income', 'Income'), ('Expense', 'Expense')], default='Expense', help_text='Input Expense / Income.', max_length=120),
        ),
    ]
