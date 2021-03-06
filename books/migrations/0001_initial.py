# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-06 08:59
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, max_length=255, null=True)),
                ('pages_amount', models.PositiveIntegerField(default=1)),
                ('source', models.FileField(upload_to='uploads/%Y/%m/%d')),
                ('is_active', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
