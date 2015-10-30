# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0004_auto_20151030_0156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='id_usuario',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=1),
        ),
        migrations.AlterField(
            model_name='transaccion',
            name='id_usuario',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]
