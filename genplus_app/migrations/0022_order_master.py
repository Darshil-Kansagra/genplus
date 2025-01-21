# Generated by Django 4.1.5 on 2023-04-01 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genplus_app', '0021_delete_order_master'),
    ]

    operations = [
        migrations.CreateModel(
            name='order_master',
            fields=[
                ('username', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('order_no', models.AutoField(primary_key=True, serialize=False)),
                ('order_name', models.CharField(max_length=50)),
                ('order_price', models.IntegerField()),
                ('order_date', models.DateField(auto_now_add=True)),
                ('order_time', models.TimeField(auto_now_add=True)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('paymethod', models.CharField(default='COD', max_length=50)),
            ],
        ),
    ]
