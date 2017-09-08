# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-05 22:56
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Changeset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min_lat', models.FloatField(default=0.0)),
                ('max_lat', models.FloatField(default=0.0)),
                ('min_lon', models.FloatField(default=0.0)),
                ('max_lon', models.FloatField(default=0.0)),
                ('tags', django.contrib.postgres.fields.jsonb.JSONField(default={})),
                ('open_datetime', models.DateTimeField(auto_now=True)),
                ('close_datetime', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]