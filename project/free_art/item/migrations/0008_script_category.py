# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-12 22:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0007_auto_20160912_2219'),
    ]

    operations = [
        migrations.AddField(
            model_name='script',
            name='category',
            field=models.ManyToManyField(to='item.Category'),
        ),
    ]