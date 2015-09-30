# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_cookie_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='cookie',
            name='service',
            field=models.CharField(default='', max_length=64),
            preserve_default=False,
        ),
    ]
