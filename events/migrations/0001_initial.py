# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-05 11:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('event_id', models.AutoField(primary_key=True, serialize=False)),
                ('event_title', models.TextField(null=True, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd1\x81\xd0\xbe\xd0\xb1\xd1\x8b\xd1\x82\xd0\xb8\xd1\x8f')),
                ('event_shortname', models.CharField(max_length=255, null=True, verbose_name=b'\xd0\x90\xd0\xb4\xd1\x80\xd0\xb5\xd1\x81')),
                ('event_date', models.DateField(null=True, verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd1\x81\xd0\xbe\xd0\xb1\xd1\x8b\xd1\x82\xd0\xb8\xd1\x8f')),
                ('event_body', models.TextField(blank=True, null=True, verbose_name=b'\xd0\x9e\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd1\x81\xd0\xbe\xd0\xb1\xd1\x8b\xd1\x82\xd0\xb8\xd1\x8f')),
                ('event_active', models.NullBooleanField(default=False, verbose_name=b'\xd0\x9f\xd1\x83\xd0\xb1\xd0\xbb\xd0\xb8\xd0\xba\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x82\xd1\x8c')),
                ('event_removed', models.NullBooleanField(default=False)),
                ('event_lang', models.CharField(max_length=2, null=True)),
            ],
            options={
                'ordering': ['pk'],
                'db_table': 'kase_events',
            },
        ),
    ]
