# Generated by Django 2.2.4 on 2019-08-16 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_model', '0007_auto_20190816_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datasource',
            name='name',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]
