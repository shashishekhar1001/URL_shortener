# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-09 11:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import shortener.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shortener', '0003_auto_20170117_1707'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer_URL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='shortener_url',
            name='url',
            field=models.CharField(max_length=220, validators=[shortener.validators.validate_url]),
        ),
        migrations.AddField(
            model_name='customer_url',
            name='paid_url',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shortener.Shortener_URL'),
        ),
    ]