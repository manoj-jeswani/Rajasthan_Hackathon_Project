# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-13 22:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kalyan', '0009_auto_20170814_0330'),
    ]

    operations = [
        migrations.AddField(
            model_name='complains',
            name='subject',
            field=models.CharField(default='Complain', max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='user_type',
            field=models.CharField(default='P', max_length=5),
        ),
        migrations.AddField(
            model_name='suggestions',
            name='subject',
            field=models.CharField(default='Suggestion', max_length=100),
        ),
    ]
