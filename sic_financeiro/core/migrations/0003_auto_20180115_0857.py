# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-15 11:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20171214_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='nome',
            field=models.CharField(db_column='nome_tag', max_length=100, unique=True),
        ),
    ]
