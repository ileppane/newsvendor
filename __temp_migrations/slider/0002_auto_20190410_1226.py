# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-04-10 11:26
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('slider', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='q',
            field=otree.db.models.PositiveIntegerField(null=True),
        ),
    ]