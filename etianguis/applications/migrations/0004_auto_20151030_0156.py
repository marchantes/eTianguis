# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0003_auto_20151030_0055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='id_usuario',
            field=models.ForeignKey(default=1, to='applications.Usuario'),
        ),
    ]
