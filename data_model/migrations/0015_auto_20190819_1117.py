# Generated by Django 2.2.4 on 2019-08-19 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data_model', '0014_auto_20190819_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stringtag',
            name='example',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='data_model.Example'),
        ),
    ]
