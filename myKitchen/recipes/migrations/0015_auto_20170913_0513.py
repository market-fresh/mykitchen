# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-13 05:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0014_auto_20170831_0738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='cover_photo',
            field=models.ImageField(blank=True, upload_to='recipes/images/'),
        ),
    ]
