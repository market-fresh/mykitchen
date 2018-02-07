# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-29 07:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_auto_20170829_0648'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipe',
            options={'ordering': ('id',)},
        ),
        migrations.AlterField(
            model_name='recipe',
            name='cover_photo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='story',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='subheader',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='video_link',
            field=models.URLField(blank=True),
        ),
    ]
