# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-04 15:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('issue', '0009_auto_20180904_1509'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='user',
            new_name='created_by',
        ),
        migrations.RenameField(
            model_name='issue',
            old_name='user',
            new_name='created_by',
        ),
    ]
