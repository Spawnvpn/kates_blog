# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-26 14:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='thumbnail',
            field=models.ImageField(blank=True, max_length=500, null=True, upload_to='photos'),
        ),
    ]
