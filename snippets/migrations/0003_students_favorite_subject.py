# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0002_auto_20150819_0949'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='favorite_subject',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
