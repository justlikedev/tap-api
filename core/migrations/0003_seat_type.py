# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-06-07 01:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20180603_2009'),
    ]

    operations = [
        migrations.AddField(
            model_name='seat',
            name='type',
            field=models.CharField(max_length=1, null=True),
        ),
    ]
