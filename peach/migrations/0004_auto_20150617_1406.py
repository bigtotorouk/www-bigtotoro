# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('peach', '0003_auto_20150613_1715'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='peach',
            options={'verbose_name': '\u6587\u7ae0 - Peach'},
        ),
        migrations.AddField(
            model_name='peach',
            name='city',
            field=models.CharField(blank=True, max_length=100, verbose_name='\u6240\u5728\u57ce\u5e02', choices=[(0, '\u5168\u56fd'), (1, '\u7701\u3001\u76f4\u8f96\u5e02'), (2, '\u5e02\u3001\u76f4\u8f96\u5e02\u533a'), (3, '\u533a\u3001\u53bf\u7b49')]),
        ),
        migrations.AlterField(
            model_name='peach',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='peach',
            name='desc',
            field=models.CharField(max_length=200, verbose_name='\u63cf\u8ff0'),
        ),
        migrations.AlterField(
            model_name='peach',
            name='favors',
            field=models.ManyToManyField(related_name='favors', verbose_name='\u6536\u85cf\u8be5\u5bf9\u8c61\u7684\u7528\u6237', to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AlterField(
            model_name='peach',
            name='img',
            field=models.ImageField(upload_to=b'peach/imgs', verbose_name='\u56fe\u7247'),
        ),
        migrations.AlterField(
            model_name='peach',
            name='likes',
            field=models.ManyToManyField(related_name='likes', verbose_name='\u559c\u6b22\u8be5\u5bf9\u8c61\u7684\u7528\u6237', to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AlterField(
            model_name='peach',
            name='location',
            field=models.OneToOneField(verbose_name='\u4f4d\u7f6e', to='peach.Location'),
        ),
        migrations.AlterField(
            model_name='peach',
            name='modify_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u4fee\u6539\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='peach',
            name='title',
            field=models.CharField(max_length=100, verbose_name='\u6807\u9898'),
        ),
    ]
