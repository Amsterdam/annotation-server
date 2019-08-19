# Generated by Django 2.2.4 on 2019-08-19 14:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('data_model', '0021_auto_20190819_1410'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stringtag',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='stringtag',
            name='modified_at',
        ),
        migrations.AddField(
            model_name='annotation',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='annotation',
            name='modified_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
