# Generated by Django 3.2.4 on 2021-06-24 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sampleapp', '0011_auto_20210624_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='Verified',
            field=models.BooleanField(default=False),
        ),
    ]
