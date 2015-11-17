# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('variables_inside_model_text_field', '0002_auto_20151117_0412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailnotification',
            name='greetings',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='emailnotification',
            name='status',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
