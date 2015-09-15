# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0005_auto_20150915_1300'),
    ]

    operations = [
        migrations.AddField(
            model_name='nutreport',
            name='suggest',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
