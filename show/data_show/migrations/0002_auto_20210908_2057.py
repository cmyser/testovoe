# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2021-09-08 17:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_show', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='data_show_company',
            new_name='company',
        ),
    ]
