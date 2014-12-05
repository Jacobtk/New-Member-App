# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apartmentaddress',
            name='address_ptr',
        ),
        migrations.RemoveField(
            model_name='apartmentaddress',
            name='generic_address',
        ),
        migrations.DeleteModel(
            name='ApartmentAddress',
        ),
        migrations.RemoveField(
            model_name='genericaddress',
            name='address_ptr',
        ),
        migrations.DeleteModel(
            name='GenericAddress',
        ),
        migrations.AddField(
            model_name='address',
            name='apartment_number',
            field=models.CharField(max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='address',
            name='area_code',
            field=models.CharField(default='-', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='address',
            name='city',
            field=models.CharField(default='-', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='address',
            name='house_number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='address',
            name='state',
            field=models.CharField(default='-', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='address',
            name='street',
            field=models.CharField(default='-', max_length=300),
            preserve_default=False,
        ),
    ]
