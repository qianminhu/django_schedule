# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_type', models.CharField(max_length=255)),
                ('frequency', models.CharField(max_length=50)),
                ('person_in_charge', models.CharField(max_length=600)),
                ('date_due', models.DateField(verbose_name=b'date due')),
            ],
        ),
    ]
