# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-24 19:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domain', '0005_auto_20170423_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domain',
            name='name',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]
