# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('find', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userkey',
            name='key',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
