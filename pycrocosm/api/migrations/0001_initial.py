# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-29 23:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nodes',
            fields=[
                ('id', models.BigIntegerField(blank=True, primary_key=True, serialize=False)),
                ('changeset', models.BigIntegerField(blank=True, null=True)),
                ('username', models.TextField(blank=True, null=True)),
                ('uid', models.IntegerField(blank=True, null=True)),
                ('visible', models.NullBooleanField()),
                ('timestamp', models.BigIntegerField(blank=True, null=True)),
                ('version', models.IntegerField(blank=True, null=True)),
                ('current', models.NullBooleanField()),
                ('tags', models.TextField(blank=True, null=True)),
                ('geom', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'portsmouth_nodes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RelationMemsN',
            fields=[
                ('id', models.BigIntegerField(blank=True, primary_key=True, serialize=False)),
                ('version', models.IntegerField(blank=True, null=True)),
                ('member', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'portsmouth_relation_mems_n',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RelationMemsR',
            fields=[
                ('id', models.BigIntegerField(blank=True, primary_key=True, serialize=False)),
                ('version', models.IntegerField(blank=True, null=True)),
                ('member', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'portsmouth_relation_mems_r',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RelationMemsW',
            fields=[
                ('id', models.BigIntegerField(blank=True, primary_key=True, serialize=False)),
                ('version', models.IntegerField(blank=True, null=True)),
                ('member', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'portsmouth_relation_mems_w',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Relations',
            fields=[
                ('id', models.BigIntegerField(blank=True, primary_key=True, serialize=False)),
                ('changeset', models.BigIntegerField(blank=True, null=True)),
                ('username', models.TextField(blank=True, null=True)),
                ('uid', models.IntegerField(blank=True, null=True)),
                ('visible', models.NullBooleanField()),
                ('timestamp', models.BigIntegerField(blank=True, null=True)),
                ('version', models.IntegerField(blank=True, null=True)),
                ('current', models.NullBooleanField()),
                ('tags', models.TextField(blank=True, null=True)),
                ('members', models.TextField(blank=True, null=True)),
                ('memberroles', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'portsmouth_relations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WayMems',
            fields=[
                ('id', models.BigIntegerField(blank=True, primary_key=True, serialize=False)),
                ('version', models.IntegerField(blank=True, null=True)),
                ('member', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'portsmouth_way_mems',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ways',
            fields=[
                ('id', models.BigIntegerField(blank=True, primary_key=True, serialize=False)),
                ('changeset', models.BigIntegerField(blank=True, null=True)),
                ('username', models.TextField(blank=True, null=True)),
                ('uid', models.IntegerField(blank=True, null=True)),
                ('visible', models.NullBooleanField()),
                ('timestamp', models.BigIntegerField(blank=True, null=True)),
                ('version', models.IntegerField(blank=True, null=True)),
                ('current', models.NullBooleanField()),
                ('tags', models.TextField(blank=True, null=True)),
                ('members', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'portsmouth_ways',
                'managed': False,
            },
        ),
    ]
