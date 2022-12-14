# Generated by Django 4.1.1 on 2022-09-16 17:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imoveis', '0009_cota_alter_casa_data_cadastro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casa',
            name='data_cadastro',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 16, 17, 5, 51, 648190, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='cota',
            name='entrada',
            field=models.FloatField(max_length=140),
        ),
        migrations.AlterField(
            model_name='cota',
            name='valor',
            field=models.FloatField(),
        ),
    ]
