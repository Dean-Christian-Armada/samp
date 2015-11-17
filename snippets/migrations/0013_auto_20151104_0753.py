# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0012_picturefolders'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='namepicture',
            name='job',
        ),
        migrations.AddField(
            model_name='namepicture',
            name='folder_path',
            field=models.ForeignKey(default=None, to='snippets.PictureFolders'),
        ),
    ]
