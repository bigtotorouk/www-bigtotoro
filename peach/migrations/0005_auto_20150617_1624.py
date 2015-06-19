# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('peach', '0004_auto_20150617_1406'),
    ]

    operations = [
        migrations.AddField(
            model_name='peach',
            name='area',
            field=models.CharField(max_length=50, verbose_name=b'\xe5\x8c\xba', blank=True),
        ),
        migrations.AddField(
            model_name='peach',
            name='province',
            field=models.CharField(max_length=50, verbose_name=b'\xe7\x9c\x81', blank=True),
        ),
        migrations.AlterField(
            model_name='peach',
            name='city',
            field=models.CharField(max_length=50, verbose_name=b'\xe5\xb8\x82', blank=True),
        ),
    ]
