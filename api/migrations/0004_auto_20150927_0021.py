# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20150927_0010'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Unames',
            new_name='Uname',
        ),
    ]
