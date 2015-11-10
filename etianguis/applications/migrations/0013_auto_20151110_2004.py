# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0012_auto_20151110_0115'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='cantidad',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, upload_to='products'),
        ),
    ]
