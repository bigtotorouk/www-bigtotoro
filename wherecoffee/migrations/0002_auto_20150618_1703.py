# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wherecoffee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coffee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name='\u540d\u79f0')),
                ('category', models.CharField(max_length=50, verbose_name='\u79cd\u7c7b', blank=True)),
                ('desc', models.CharField(max_length=200, verbose_name='\u8be6\u60c5\u4ecb\u7ecd', blank=True)),
            ],
            options={
                'verbose_name': '\u4ea7\u54c1 - Coffee',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='state',
            field=models.CharField(blank=True, max_length=100, verbose_name='\u72b6\u6001', choices=[[b'0', b'\xe6\x96\xb0\xe5\xbb\xba'], [b'1', b'\xe8\xbf\x9b\xe8\xa1\x8c\xe4\xb8\xad'], [b'2', b'\xe5\xae\x8c\xe6\x88\x90']]),
        ),
    ]
