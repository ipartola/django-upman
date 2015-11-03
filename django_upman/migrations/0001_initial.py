# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_upman.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageUpload',
            fields=[
                ('checksum', models.CharField(max_length=64, serialize=False, primary_key=True)),
                ('category', models.CharField(default='', max_length=255, db_index=True)),
                ('name', models.CharField(max_length=255)),
                ('content_type', models.CharField(default='applicaiton/binary', max_length=255)),
                ('size', models.BigIntegerField(default=0)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('upload', models.ImageField(height_field='height', width_field='width', upload_to=django_upman.models._upload_to)),
                ('height', models.PositiveIntegerField(default=0)),
                ('width', models.PositiveIntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('checksum', models.CharField(max_length=64, serialize=False, primary_key=True)),
                ('category', models.CharField(default='', max_length=255, db_index=True)),
                ('name', models.CharField(max_length=255)),
                ('content_type', models.CharField(default='applicaiton/binary', max_length=255)),
                ('size', models.BigIntegerField(default=0)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('upload', models.FileField(upload_to=django_upman.models._upload_to)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
