# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-23 01:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients_app', '0002_auto_20160323_0156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='middle_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
