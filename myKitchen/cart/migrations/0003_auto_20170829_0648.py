# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-29 06:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_auto_20170825_1844'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='box',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='purchased',
            name='slug',
        ),
    ]