# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0004_auto_20150901_1130'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavoriteNumber',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('favorite_number', models.PositiveSmallIntegerField()),
            ],
        ),
    ]
