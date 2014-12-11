# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_member_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='date_of_birth',
            field=models.CharField(default="None", max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='email',
            field=models.EmailField(max_length=70, null=True, blank=True),
            preserve_default=True,
        ),
    ]
