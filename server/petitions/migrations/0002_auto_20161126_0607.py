# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-26 06:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('petitions', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Like',
            new_name='PetitionLike',
        ),
    ]
