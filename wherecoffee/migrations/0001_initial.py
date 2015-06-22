# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nicker', models.CharField(max_length=50, verbose_name='\u79f0\u547c')),
                ('location', models.CharField(max_length=100, verbose_name='\u5730\u5740')),
                ('tel', models.CharField(max_length=50, verbose_name='\u7535\u8bdd(\u8054\u7cfb\u65b9\u5f0f)')),
                ('licence', models.CharField(max_length=100, verbose_name='\u5e8f\u5217\u53f7', blank=True)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('modify_time', models.DateTimeField(auto_now_add=True, verbose_name='\u4fee\u6539\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u8ba2\u5355 - Coffee',
            },
        ),
    ]
