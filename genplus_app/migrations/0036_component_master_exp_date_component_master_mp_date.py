# Generated by Django 4.1.5 on 2023-04-08 13:09

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('genplus_app', '0035_delete_gamespc'),
    ]

    operations = [
        migrations.AddField(
            model_name='component_master',
            name='exp_date',
            field=models.DateField(default=datetime.datetime(2023, 11, 4, 18, 38, 48, 50720)),
        ),
        migrations.AddField(
            model_name='component_master',
            name='mp_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
