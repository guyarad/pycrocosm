# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-05 21:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20170905_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='languages',
            field=models.TextField(default=''),
        ),
    ]