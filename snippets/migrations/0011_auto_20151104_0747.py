# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import snippets.models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0010_namepicture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='namepicture',
            name='picture',
            field=models.ImageField(upload_to=snippets.models.content_file_name, blank=True),
        ),
    ]
