# Generated by Django 4.1.5 on 2023-03-31 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genplus_app', '0017_delete_card_payment'),
    ]

    operations = [
        migrations.CreateModel(
            name='card_payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CardNumber', models.IntegerField(verbose_name=16)),
                ('CardHolder', models.CharField(max_length=16)),
                ('expiresmonth', models.IntegerField(verbose_name=2)),
                ('expiresyear', models.IntegerField(verbose_name=4)),
                ('cvv', models.IntegerField(verbose_name=3)),
                ('balance', models.PositiveIntegerField(verbose_name=50)),
            ],
        ),
    ]
