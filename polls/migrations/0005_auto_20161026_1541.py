# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-26 08:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20161026_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='image',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]
