# Generated by Django 4.1.5 on 2023-04-04 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('genplus_app', '0026_alter_contactfrom_username'),
    ]

    operations = [
        migrations.DeleteModel(
            name='city_master',
        ),
        migrations.DeleteModel(
            name='state_master',
        ),
    ]
