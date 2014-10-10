# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApiKey',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('api_key', models.CharField(max_length=256)),
                ('current_status', models.IntegerField(default=1)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Coords',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('coords', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('user_api', models.ForeignKey(to='app.ApiKey')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
