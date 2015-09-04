# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0008_auto_20150903_1240'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='commoninfo_ptr',
        ),
        migrations.DeleteModel(
            name='CommonInfo',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
