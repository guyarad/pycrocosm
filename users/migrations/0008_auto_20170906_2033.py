# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-06 20:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_remove_userdata_mapid'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserPreferences',
            new_name='UserPreference',
        ),
    ]
