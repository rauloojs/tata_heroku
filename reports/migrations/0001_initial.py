# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('doc_name', models.CharField(max_length=100)),
                ('patient_name', models.CharField(max_length=100)),
                ('consult_date', models.DateTimeField(verbose_name=b'date consulted')),
                ('patient_state', models.CharField(max_length=200)),
                ('observ', models.CharField(max_length=500)),
                ('suggest', models.CharField(max_length=500)),
            ],
        ),
    ]
