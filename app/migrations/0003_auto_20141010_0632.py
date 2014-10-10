# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20141010_0541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coords',
            name='status',
            field=models.IntegerField(default=1),
        ),
    ]
