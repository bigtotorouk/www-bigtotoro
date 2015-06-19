# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('peach', '0002_auto_20150613_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peach',
            name='favors',
            field=models.ManyToManyField(related_name='favors', to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AlterField(
            model_name='peach',
            name='likes',
            field=models.ManyToManyField(related_name='likes', to=settings.AUTH_USER_MODEL, blank=True),
        ),
    ]
