# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-11-28 23:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoreo', '0002_auto_20181003_1052'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrosensores',
            name='idLocal',
            field=models.FloatField(null=True),
        ),
    ]