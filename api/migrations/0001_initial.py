# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name=b'Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name=b'Modified at')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'BaseModel',
                'verbose_name_plural': 'BaseModels',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ApartmentAddress',
            fields=[
                ('address_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='api.Address')),
                ('apartment_number', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'BaseModel',
                'verbose_name_plural': 'BaseModels',
            },
            bases=('api.address',),
        ),
        migrations.CreateModel(
            name='ChurchUnit',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name=b'Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name=b'Modified at')),
                ('id', models.IntegerField(serialize=False, primary_key=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'BaseModel',
                'verbose_name_plural': 'BaseModels',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CustomField',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name=b'Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name=b'Modified at')),
                ('index', models.IntegerField()),
                ('field_name', models.CharField(max_length=300)),
                ('unit', models.ForeignKey(to='api.ChurchUnit')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'BaseModel',
                'verbose_name_plural': 'BaseModels',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CustomFieldEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name=b'Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name=b'Modified at')),
                ('contents', models.CharField(max_length=300)),
                ('field', models.ForeignKey(to='api.CustomField')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'BaseModel',
                'verbose_name_plural': 'BaseModels',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GenericAddress',
            fields=[
                ('address_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='api.Address')),
                ('house_number', models.IntegerField()),
                ('street', models.CharField(max_length=300)),
                ('city', models.CharField(max_length=300)),
                ('state', models.CharField(max_length=300)),
                ('area_code', models.CharField(max_length=300)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'BaseModel',
                'verbose_name_plural': 'BaseModels',
            },
            bases=('api.address',),
        ),
        migrations.CreateModel(
            name='MembershipEntity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name=b'Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name=b'Modified at')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'BaseModel',
                'verbose_name_plural': 'BaseModels',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('membershipentity_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='api.MembershipEntity')),
                ('full_name', models.CharField(max_length=300)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'BaseModel',
                'verbose_name_plural': 'BaseModels',
            },
            bases=('api.membershipentity',),
        ),
        migrations.CreateModel(
            name='Household',
            fields=[
                ('membershipentity_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='api.MembershipEntity')),
                ('status', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=11)),
                ('address', models.ForeignKey(to='api.Address')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'BaseModel',
                'verbose_name_plural': 'BaseModels',
            },
            bases=('api.membershipentity',),
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name=b'Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name=b'Modified at')),
                ('membership_entity', models.ForeignKey(to='api.MembershipEntity')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'BaseModel',
                'verbose_name_plural': 'BaseModels',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='customfieldentry',
            name='survey',
            field=models.ForeignKey(to='api.Survey'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='churchunit',
            name='bishop',
            field=models.ForeignKey(to='api.Member'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='apartmentaddress',
            name='generic_address',
            field=models.ForeignKey(to='api.GenericAddress'),
            preserve_default=True,
        ),
    ]
