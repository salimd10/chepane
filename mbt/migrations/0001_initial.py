# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-17 23:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('price', models.IntegerField(default=0)),
                ('description', models.TextField(default=b'', null=True)),
                ('imageurl', models.ImageField(upload_to=b'mbt/media/dishes')),
                ('views', models.IntegerField(default=0)),
                ('likes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='market',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.TextField(default=b'', max_length=255, unique=True)),
                ('phone', models.CharField(max_length=11)),
                ('email', models.EmailField(default=b'', max_length=254, null=True)),
                ('visited', models.IntegerField(default=0)),
                ('likes', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='market',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mbt.market'),
        ),
    ]
