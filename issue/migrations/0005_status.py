# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-03 16:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issue', '0004_varieties'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('To do', 'To do'), ('Doing', 'Doing'), ('Done', 'Done')], default='To do', max_length=2)),
            ],
        ),
    ]