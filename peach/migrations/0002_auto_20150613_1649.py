# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('peach', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('parent_id', models.IntegerField()),
                ('name', models.CharField(max_length=30)),
                ('type', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Peach',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=200)),
                ('img', models.ImageField(upload_to=b'peach/imgs')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('modify_time', models.DateTimeField(auto_now_add=True)),
                ('favors', models.ManyToManyField(related_name='favors', to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(related_name='likes', to=settings.AUTH_USER_MODEL)),
                ('location', models.OneToOneField(to='peach.Location')),
            ],
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
