# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-13 05:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='country',
            field=models.TextField(blank=True, default='Singapore', max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, upload_to='users/images/'),
        ),
    ]
