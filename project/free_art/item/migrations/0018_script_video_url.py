# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-14 23:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0017_script_shutter_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='script',
            name='video_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]