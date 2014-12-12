# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_churchunit_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='status',
            field=models.CharField(default=b'new', max_length=15),
            preserve_default=True,
        ),
    ]
