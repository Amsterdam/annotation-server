# Generated by Django 2.2.4 on 2019-08-19 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_model', '0016_annotation_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='annotation',
            name='tag',
        ),
    ]
