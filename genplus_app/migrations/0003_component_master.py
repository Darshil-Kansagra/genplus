# Generated by Django 4.1.5 on 2023-03-26 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('genplus_app', '0002_category_master'),
    ]

    operations = [
        migrations.CreateModel(
            name='component_master',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('con_name', models.CharField(max_length=350)),
                ('con_price', models.IntegerField()),
                ('con_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='genplus_app.category_master', verbose_name='cat_id')),
            ],
        ),
    ]
