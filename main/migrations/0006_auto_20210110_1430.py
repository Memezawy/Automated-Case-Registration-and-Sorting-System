# Generated by Django 3.1.5 on 2021-01-10 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20210109_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='refugee',
            name='file_no',
            field=models.CharField(max_length=12),
        ),
    ]