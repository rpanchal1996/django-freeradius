# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-11 09:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_freeradius', '0012_auto_20171206_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='radiuscheck',
            name='attribute',
            field=models.CharField(blank=True, choices=[('NT-Password', 'NT-Password')], default='NT-Password', max_length=64, verbose_name='attribute'),
        ),
    ]
