# Generated by Django 4.1.5 on 2023-04-08 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genplus_app', '0030_delete_laptop_master_delete_pc_master'),
    ]

    operations = [
        migrations.CreateModel(
            name='games',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gameimg', models.ImageField(height_field=230, upload_to='images/', width_field=230)),
                ('gamename', models.CharField(max_length=50)),
            ],
        ),
    ]
