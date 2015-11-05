# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0006_auto_20151105_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='fecha_publicacion',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
