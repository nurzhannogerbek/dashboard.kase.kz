# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-06 08:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slider', '0004_auto_20171206_0532'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='slide',
            options={'ordering': ['idx', 'pk'], 'permissions': (('view_slide', 'Can view slides'), ('view_slide_change_history', 'Can view change history of the slide'), ('revert_slide', 'Can revert slides'))},
        ),
    ]
