# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_item_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubLocation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='sublocation',
            field=models.ForeignKey(to='inventory.SubLocation', null=True),
        ),
    ]
