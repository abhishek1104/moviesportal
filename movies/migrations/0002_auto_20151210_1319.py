# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_movies_model_v1'),
    ]

    operations = [
        migrations.AddField(
            model_name='heroens',
            name='name',
            field=models.CharField(default='PleaseEnter', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='heros',
            name='name',
            field=models.CharField(default=datetime.datetime(2015, 12, 10, 7, 49, 13, 925000, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movies',
            name='name',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
    ]
