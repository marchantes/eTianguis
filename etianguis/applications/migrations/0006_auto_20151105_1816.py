# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0005_auto_20151030_0223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='fecha_publicacion',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 5, 18, 16, 48, 123938)),
        ),
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, upload_to='', null=True),
        ),
    ]
