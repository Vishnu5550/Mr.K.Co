# Generated by Django 3.2.4 on 2021-07-05 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sampleapp', '0023_campaigndetail_categoary'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaigndocuments',
            name='Title',
            field=models.CharField(default='Empty', max_length=54),
            preserve_default=False,
        ),
    ]
