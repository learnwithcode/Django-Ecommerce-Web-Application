# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-09-26 11:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_featured'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='featured',
        ),
    ]
