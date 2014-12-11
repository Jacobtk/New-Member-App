# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_member_unit'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='phone',
            field=models.CharField(default='none', max_length=11),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='preferred_name',
            field=models.CharField(max_length=300, null=True, blank=True),
            preserve_default=True,
        ),
    ]
