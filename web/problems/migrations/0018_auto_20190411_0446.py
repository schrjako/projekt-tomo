# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2019-04-11 04:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("problems", "0017_auto_20171104_1335"),
    ]

    operations = [
        migrations.AlterField(
            model_name="historicalproblem",
            name="language",
            field=models.CharField(
                choices=[
                    ("python", "Python 3"),
                    ("octave", "Octave/Matlab"),
                    ("r", "R"),
                ],
                default="python",
                max_length=8,
            ),
        ),
        migrations.AlterField(
            model_name="problem",
            name="language",
            field=models.CharField(
                choices=[
                    ("python", "Python 3"),
                    ("octave", "Octave/Matlab"),
                    ("r", "R"),
                ],
                default="python",
                max_length=8,
            ),
        ),
    ]
