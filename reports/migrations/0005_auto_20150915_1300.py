# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0004_auto_20150908_0757'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nutreport',
            old_name='diet',
            new_name='glucosa',
        ),
        migrations.RenameField(
            model_name='nutreport',
            old_name='risk_factors',
            new_name='imc',
        ),
    ]
