# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wherecoffee', '0003_auto_20150618_1708'),
    ]

    operations = [
        migrations.AddField(
            model_name='coffee',
            name='img0',
            field=models.ImageField(upload_to=b'wherecoffee/coffee/', verbose_name='\u56fe\u72471', blank=True),
        ),
        migrations.AddField(
            model_name='coffee',
            name='img1',
            field=models.ImageField(upload_to=b'wherecoffee/coffee/', verbose_name='\u56fe\u72472', blank=True),
        ),
        migrations.AddField(
            model_name='coffee',
            name='img2',
            field=models.ImageField(upload_to=b'wherecoffee/coffee/', verbose_name='\u56fe\u72473', blank=True),
        ),
        migrations.AddField(
            model_name='coffee',
            name='price_new',
            field=models.FloatField(default=0.0, verbose_name='\u73b0\u4ef7', blank=True),
        ),
        migrations.AddField(
            model_name='coffee',
            name='price_old',
            field=models.FloatField(default=0.0, verbose_name='\u539f\u4ef7', blank=True),
        ),
    ]
