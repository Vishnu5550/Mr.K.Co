# Generated by Django 3.2.4 on 2021-06-30 00:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sampleapp', '0019_auto_20210630_0520'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campaign',
            name='File',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='Image',
        ),
    ]
