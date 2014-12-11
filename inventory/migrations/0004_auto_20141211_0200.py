# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20141211_0015'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='count',
            new_name='stock',
        ),
    ]
