# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_cookie'),
    ]

    operations = [
        migrations.AddField(
            model_name='cookie',
            name='username',
            field=models.CharField(default='', max_length=32),
            preserve_default=False,
        ),
    ]
