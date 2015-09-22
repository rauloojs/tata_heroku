# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0006_nutreport_suggest'),
    ]

    operations = [
        migrations.CreateModel(
            name='FisReport',
            fields=[
                ('report', models.OneToOneField(primary_key=True, serialize=False, to='reports.Report')),
                ('ter_ocup', models.TextField()),
                ('ter_man', models.TextField()),
                ('masaje', models.TextField()),
                ('evol_pac', models.TextField()),
                ('recom', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='GerReport',
            fields=[
                ('report', models.OneToOneField(primary_key=True, serialize=False, to='reports.Report')),
                ('tratamiento', models.TextField()),
                ('suggest', models.TextField()),
            ],
        ),
    ]
