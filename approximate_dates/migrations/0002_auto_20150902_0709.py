# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_date_extensions.fields


class Migration(migrations.Migration):

    dependencies = [
        ('approximate_dates', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='samplemonthdate',
            name='birthdate',
            field=django_date_extensions.fields.ApproximateDateField(default=None, max_length=10),
        ),
        migrations.AlterField(
            model_name='samplemonthdate',
            name='date',
            field=models.DateField(default=None),
        ),
    ]
