# Generated by Django 3.1.5 on 2021-01-11 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20210110_1930'),
    ]

    operations = [
        migrations.AddField(
            model_name='refugee',
            name='case_status',
            field=models.BooleanField(default=False),
        ),
    ]