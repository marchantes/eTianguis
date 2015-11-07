# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0008_auto_20151107_0242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='id_usuario',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
        ),
    ]
