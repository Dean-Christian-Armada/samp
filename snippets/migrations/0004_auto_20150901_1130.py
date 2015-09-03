# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0003_students_favorite_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavoriteSubject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('favorite_subject', models.CharField(default=None, max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='students',
            name='favorite_subject',
            field=models.ForeignKey(to='snippets.FavoriteSubject'),
        ),
    ]
