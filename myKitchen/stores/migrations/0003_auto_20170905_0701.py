# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-05 07:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0002_auto_20170829_0648'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingredients',
            old_name='collection_type',
            new_name='collection',
        ),
    ]
