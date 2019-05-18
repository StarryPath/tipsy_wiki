# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-18 13:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0002_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='team',
            options={'ordering': ['name'], 'verbose_name': '团队', 'verbose_name_plural': '团队'},
        ),
        migrations.AddField(
            model_name='team',
            name='intro',
            field=models.TextField(default='', verbose_name='团队简介'),
        ),
    ]
