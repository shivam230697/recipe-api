# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-02-11 12:59
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('obj', django.db.models.manager.Manager()),
            ],
        ),
    ]