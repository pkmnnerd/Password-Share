# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Relation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sharer', models.CharField(max_length=255)),
                ('moocher', models.CharField(max_length=255)),
                ('service', models.CharField(max_length=255)),
            ],
        ),
    ]
