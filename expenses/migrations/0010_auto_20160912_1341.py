# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-12 13:41
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import expenses.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('expenses', '0009_default_groups_creation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(blank=True, max_length=50, null=True)),
                ('date', models.DateField(default=datetime.date.today)),
                ('time', models.TimeField(blank=True, default=expenses.models.current_time, null=True)),
                ('cost', models.FloatField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='item',
            name='user',
        ),
        migrations.DeleteModel(
            name='Item',
        ),
    ]
