# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-11 07:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20170829_0826'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('address_type', models.CharField(choices=[('1', 'Billing'), ('2', 'Shipping')], max_length=1)),
                ('address_1', models.CharField(max_length=50)),
                ('address_2', models.CharField(blank=True, max_length=50)),
                ('country', models.CharField(default='Singapore', max_length=50)),
                ('city', models.CharField(default='Singapore', max_length=50)),
                ('unit_no', models.CharField(blank=True, max_length=10)),
                ('postal_code', models.CharField(max_length=6)),
                ('contact_no', models.CharField(blank=True, max_length=15)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Profile')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
