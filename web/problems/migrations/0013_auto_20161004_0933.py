# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-10-04 09:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("problems", "0012_auto_20161004_0927"),
    ]

    operations = [
        migrations.AddField(
            model_name="historicalpart",
            name="template",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="part",
            name="template",
            field=models.TextField(blank=True),
        ),
    ]
