# Generated by Django 3.2.4 on 2021-06-25 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sampleapp', '0015_auto_20210625_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='Amount_Reached',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='Amount_Wanted',
            field=models.IntegerField(default=0),
        ),
    ]
