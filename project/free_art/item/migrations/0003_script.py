# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-12 21:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_auto_20160912_2126'),
    ]

    operations = [
        migrations.CreateModel(
            name='Script',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('short_desc', models.TextField()),
                ('full_desc', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
