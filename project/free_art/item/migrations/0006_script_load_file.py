# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-12 22:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0005_auto_20160912_2214'),
    ]

    operations = [
        migrations.AddField(
            model_name='script',
            name='load_file',
            field=models.FileField(blank=True, null=True, upload_to='script/file'),
        ),
    ]