# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-10 07:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0006_customer_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer_url',
            name='clicks',
            field=models.IntegerField(default=0),
        ),
    ]
