# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-29 06:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='settings',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='settings_group',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='social_media',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='user_settings',
            name='slug',
        ),
    ]