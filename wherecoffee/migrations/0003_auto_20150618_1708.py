# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wherecoffee', '0002_auto_20150618_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='coffee',
            field=models.ForeignKey(verbose_name='\u5496\u5561', blank=True, to='wherecoffee.Coffee', null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='state',
            field=models.CharField(blank=True, max_length=100, verbose_name='\u72b6\u6001', choices=[[b'0', '\u65b0\u5efa'], [b'1', '\u8fdb\u884c\u4e2d'], [b'2', '\u5b8c\u6210']]),
        ),
    ]
