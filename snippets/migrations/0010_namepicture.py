# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0009_auto_20150903_1257'),
    ]

    operations = [
        migrations.CreateModel(
            name='NamePicture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=None, max_length=50)),
                ('job', models.CharField(default=None, max_length=50)),
                ('picture', models.ImageField(upload_to=b'dynamic-folder-pictures', blank=True)),
            ],
        ),
    ]
