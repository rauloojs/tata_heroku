# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0003_auto_20150906_2130'),
    ]

    operations = [
        migrations.CreateModel(
            name='NutReport',
            fields=[
                ('report', models.OneToOneField(primary_key=True, serialize=False, to='reports.Report')),
                ('weight', models.FloatField()),
                ('height', models.FloatField()),
                ('pressure', models.TextField()),
                ('risk_factors', models.TextField()),
                ('appetite', models.TextField()),
                ('diet', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PsyReport',
            fields=[
                ('report', models.OneToOneField(primary_key=True, serialize=False, to='reports.Report')),
                ('patient_state', models.CharField(max_length=200)),
                ('suggest', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='report',
            name='patient_state',
        ),
        migrations.RemoveField(
            model_name='report',
            name='suggest',
        ),
        migrations.AddField(
            model_name='report',
            name='report_type',
            field=models.CharField(default='', max_length=15),
            preserve_default=False,
        ),
    ]
