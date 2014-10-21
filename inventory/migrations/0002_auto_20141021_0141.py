# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='loans',
            field=models.ManyToManyField(to=b'inventory.Item', through='inventory.Loan', blank=True),
        ),
        migrations.AlterField(
            model_name='loan',
            name='return_date',
            field=models.DateTimeField(blank=True),
        ),
    ]
