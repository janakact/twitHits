# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0002_auto_20150106_1852'),
    ]

    operations = [
        migrations.AddField(
            model_name='twitteruser',
            name='user_id',
            field=models.CharField(max_length=1000, default=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='twitteruser',
            name='access_key',
            field=models.CharField(max_length=1000, default=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='twitteruser',
            name='access_secret',
            field=models.CharField(max_length=1000, default=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='twitteruser',
            name='user_name',
            field=models.CharField(max_length=100, default=''),
            preserve_default=True,
        ),
    ]
