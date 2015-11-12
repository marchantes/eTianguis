# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0007_auto_20151105_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='id_usuario',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(default=1, upload_to=b'products', blank=True),
            preserve_default=False,
        ),
    ]
