# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0002_auto_20150825_0732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='observ',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='report',
            name='suggest',
            field=models.TextField(),
        ),
    ]
