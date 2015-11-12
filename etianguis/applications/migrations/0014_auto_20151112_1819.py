# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0013_auto_20151110_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='cantidad',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='transaccion',
            name='cantidad',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='transaccion',
            name='fecha',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='transaccion',
            name='id_usuario',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=1),
        ),
    ]
