# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-26 16:45
from __future__ import unicode_literals

import contentcuration.models
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('contentcuration', '0026_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='assessmentitem',
            name='assessment_id',
            field=contentcuration.models.UUIDField(default=uuid.uuid4, editable=False, max_length=32),
        ),
        migrations.AlterField(
            model_name='contentnode',
            name='license',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='contentcuration.License'),
        ),
    ]
