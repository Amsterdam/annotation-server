# Generated by Django 2.2.4 on 2019-08-19 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data_model', '0017_remove_annotation_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='annotation',
            name='tag',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='data_model.StringTag'),
            preserve_default=False,
        ),
    ]
