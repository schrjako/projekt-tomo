# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-10-04 09:27
from __future__ import unicode_literals

import utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("problems", "0011_auto_20160203_2250"),
    ]

    operations = [
        migrations.AlterField(
            model_name="historicalpart",
            name="secret",
            field=models.TextField(
                default="[]", validators=[utils.is_json_string_list]
            ),
        ),
        migrations.AlterField(
            model_name="historicalproblem",
            name="language",
            field=models.CharField(
                choices=[("python", "Python 3"), ("octave", "Octave")],
                default="python",
                max_length=8,
            ),
        ),
        migrations.AlterField(
            model_name="part",
            name="secret",
            field=models.TextField(
                default="[]", validators=[utils.is_json_string_list]
            ),
        ),
        migrations.AlterField(
            model_name="problem",
            name="language",
            field=models.CharField(
                choices=[("python", "Python 3"), ("octave", "Octave")],
                default="python",
                max_length=8,
            ),
        ),
    ]
