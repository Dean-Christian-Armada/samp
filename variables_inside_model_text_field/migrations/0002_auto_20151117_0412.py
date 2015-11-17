# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('variables_inside_model_text_field', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailnotification',
            name='message',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
