# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20141205_0709'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='unit',
            field=models.ForeignKey(default=0, to='api.ChurchUnit'),
            preserve_default=False,
        ),
    ]
