# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-23 07:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('linux', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='linux',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='linux',
            name='last_modify_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
