# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-06 05:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('static_pages', '0003_auto_20171123_0546'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='staticpage',
            options={'ordering': ['idx', 'pk'], 'permissions': (('view_staticpage', 'Can view static pages'), ('view_staticpage_change_history', 'Can view change history of the static page'))},
        ),
    ]
