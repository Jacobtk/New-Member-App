# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20141205_0702'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='house_number',
        ),
        migrations.AddField(
            model_name='address',
            name='house',
            field=models.CharField(default='-', max_length=300),
            preserve_default=False,
        ),
    ]
