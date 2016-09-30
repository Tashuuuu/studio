# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-19 23:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contentcuration', '0019_auto_20160919_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assessmentitem',
            name='exercise',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='all_assessment_items', to='contentcuration.Exercise'),
        ),
    ]
