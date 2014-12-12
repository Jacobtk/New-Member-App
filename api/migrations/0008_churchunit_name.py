# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20141211_0104'),
    ]

    operations = [
        migrations.AddField(
            model_name='churchunit',
            name='name',
            field=models.CharField(default='none', max_length=50),
            preserve_default=False,
        ),
    ]
