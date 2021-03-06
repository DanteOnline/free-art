# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-12 21:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='category/other')),
            ],
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(upload_to='category/main'),
        ),
        migrations.AddField(
            model_name='categoryimage',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='item.Category'),
        ),
    ]
