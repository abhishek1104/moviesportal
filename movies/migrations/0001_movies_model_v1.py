# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='heroens',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='heros',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='movies',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('release_date', models.DateField()),
                ('genere_choices', models.CharField(max_length=20, choices=[(b'Action', b'Action'), (b'Animation', b'Animation'), (b'Sci-Fi', b'Sci-Fi'), (b'Documentry', b'Documentry'), (b'Family', b'Family'), (b'Horror', b'Horror'), (b'Comedy', b'Comedy')])),
                ('heroens', models.ForeignKey(to='movies.heroens')),
                ('heroes', models.ForeignKey(to='movies.heros')),
            ],
        ),
    ]
