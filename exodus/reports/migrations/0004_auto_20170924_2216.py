# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-24 22:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0003_auto_20170924_2215'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dnsquery',
            old_name='is_trackersdfdsf',
            new_name='is_tracker',
        ),
    ]
