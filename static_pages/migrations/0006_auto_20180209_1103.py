# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-09 11:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('static_pages', '0005_auto_20171206_0819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staticpage',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True, unique=True, verbose_name=b'\xd0\xa7\xd0\x9f\xd0\xa3'),
        ),
    ]
