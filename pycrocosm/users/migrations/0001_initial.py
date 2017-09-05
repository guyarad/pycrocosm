# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-05 21:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_lat', models.FloatField()),
                ('home_lon', models.FloatField()),
                ('home_zoom', models.IntegerField(default=-1)),
                ('userid', models.IntegerField(default=-1)),
                ('description', models.TextField()),
                ('languages', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]