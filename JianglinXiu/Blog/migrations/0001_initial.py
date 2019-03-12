# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('excerpt', models.CharField(max_length=200)),
                ('updatetime', models.DateField()),
                ('imageadress', models.TextField()),
            ],
        ),
    ]
