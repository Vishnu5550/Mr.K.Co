# Generated by Django 3.2.4 on 2021-07-03 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sampleapp', '0021_campaign_categoary'),
    ]

    operations = [
        migrations.CreateModel(
            name='CampaignDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=54)),
                ('Title', models.CharField(max_length=54, null=True)),
                ('SubTitle', models.CharField(max_length=54, null=True)),
                ('Description', models.CharField(max_length=2000, null=True)),
                ('Amount_Wanted', models.IntegerField(null=True)),
                ('Amount_Reached', models.IntegerField(null=True)),
                ('Verified', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='CampaignDocuments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=54)),
                ('Documents', models.FileField(blank=True, upload_to='files_db')),
            ],
        ),
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Address', models.CharField(max_length=200)),
                ('Permanent_Address', models.CharField(max_length=200)),
                ('Date_Of_Birth', models.CharField(max_length=20)),
                ('FirstName', models.CharField(max_length=50)),
                ('LastName', models.CharField(max_length=200)),
                ('Description', models.CharField(max_length=500)),
                ('Country', models.CharField(max_length=100)),
                ('State', models.CharField(max_length=100)),
                ('Gender', models.CharField(max_length=20)),
                ('Pin_Code', models.IntegerField(null=True)),
                ('Country_code', models.IntegerField(null=True)),
                ('Phone_Number', models.IntegerField(null=True)),
                ('Verified', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='Campaign',
        ),
    ]
