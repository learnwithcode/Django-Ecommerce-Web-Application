# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-09-26 11:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_product_featured'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='featured',
        ),
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('normal', 'Normal'), ('featured', 'Featured')], default='normal', max_length=10),
        ),
    ]
