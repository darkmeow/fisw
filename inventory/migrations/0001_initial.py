# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rut', models.CharField(max_length=15)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('purchase_date', models.DateTimeField()),
                ('count', models.IntegerField(default=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Instrument',
            fields=[
                ('item_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='inventory.Item')),
            ],
            options={
            },
            bases=('inventory.item',),
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('loan_date', models.DateTimeField(auto_now=True)),
                ('return_date', models.DateTimeField()),
                ('is_active', models.BooleanField(default=True)),
                ('client', models.ForeignKey(to='inventory.Client')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('administrator', models.ForeignKey(to='inventory.Administrator')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('item_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='inventory.Item')),
            ],
            options={
            },
            bases=('inventory.item',),
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_joined', models.DateField()),
                ('client', models.ForeignKey(to='inventory.Client')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('brief', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('start_date', models.DateTimeField(verbose_name=b'start date')),
                ('is_active', models.BooleanField(default=True)),
                ('manager', models.ForeignKey(to='inventory.Client')),
                ('members', models.ManyToManyField(related_name=b'inventory_project_related', through='inventory.Membership', to='inventory.Client')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('item_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='inventory.Item')),
            ],
            options={
            },
            bases=('inventory.item',),
        ),
        migrations.AddField(
            model_name='membership',
            name='project',
            field=models.ForeignKey(to='inventory.Project'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='loan',
            name='item',
            field=models.ForeignKey(to='inventory.Item'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='item',
            name='location',
            field=models.ForeignKey(to='inventory.Location'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='client',
            name='loans',
            field=models.ManyToManyField(to='inventory.Item', through='inventory.Loan'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='client',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
