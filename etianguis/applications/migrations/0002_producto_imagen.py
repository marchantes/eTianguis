# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(default=datetime.datetime(2015, 10, 29, 2, 14, 46, 713080, tzinfo=utc), upload_to=b''),
            preserve_default=False,
        ),
    ]
