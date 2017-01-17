# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-17 11:37
from __future__ import unicode_literals

from django.db import migrations, models
import shortener.validators


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0002_auto_20170112_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortener_url',
            name='url',
            field=models.CharField(max_length=220, validators=[shortener.validators.validate_url, shortener.validators.dot_com_validator]),
        ),
    ]