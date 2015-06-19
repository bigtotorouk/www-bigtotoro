# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('peach', '0005_auto_20150617_1624'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='peach',
            name='location',
        ),
    ]
