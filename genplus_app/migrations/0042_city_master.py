# Generated by Django 4.1.5 on 2023-04-08 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genplus_app', '0041_delete_city'),
    ]

    operations = [
        migrations.CreateModel(
            name='city_master',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
