# Generated by Django 3.2.4 on 2021-06-30 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sampleapp', '0020_auto_20210630_0535'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='Categoary',
            field=models.CharField(default='other', max_length=100),
            preserve_default=False,
        ),
    ]
