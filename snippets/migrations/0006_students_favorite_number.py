# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0005_favoritenumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='favorite_number',
            field=models.ForeignKey(default=1, to='snippets.FavoriteNumber'),
        ),
    ]
