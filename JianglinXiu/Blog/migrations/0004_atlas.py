# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0003_blog_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Atlas',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('updatetime', models.DateField(null=True)),
                ('imageadress', models.TextField()),
                ('img', models.ImageField(default='none', upload_to='upload')),
            ],
        ),
    ]
