# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-23 15:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_team_coaches'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='age_category',
        ),
    ]
