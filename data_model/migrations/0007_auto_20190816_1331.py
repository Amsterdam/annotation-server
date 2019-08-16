# Generated by Django 2.2.4 on 2019-08-16 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_model', '0006_annotation_example'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataSource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.AlterField(
            model_name='example',
            name='reference',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]
