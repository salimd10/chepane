# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-02 00:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mbt', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='market',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
