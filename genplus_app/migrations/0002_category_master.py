# Generated by Django 4.1.5 on 2023-03-26 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genplus_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='category_master',
            fields=[
                ('cat_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='cat_id')),
                ('cat_name', models.CharField(max_length=350)),
            ],
        ),
    ]
