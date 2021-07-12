# Generated by Django 3.2.4 on 2021-06-24 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sampleapp', '0008_alter_register_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Address', models.CharField(max_length=200)),
                ('Permanent_Address', models.CharField(max_length=200)),
                ('Date_Of_Birth', models.CharField(max_length=20)),
                ('Title', models.CharField(max_length=50)),
                ('Sub_Title', models.CharField(max_length=200)),
                ('Description', models.CharField(max_length=500)),
                ('Country', models.CharField(max_length=100)),
                ('State', models.CharField(max_length=100)),
                ('Gender', models.CharField(max_length=20)),
                ('Pin_Code', models.IntegerField()),
                ('Phone_Number', models.IntegerField()),
                ('Image_1', models.ImageField(upload_to='pics')),
                ('Image_2', models.ImageField(upload_to='pics')),
                ('Document_per1', models.FileField(upload_to='files_db')),
                ('Document_per2', models.FileField(upload_to='files_db')),
                ('Document_ver1', models.FileField(upload_to='files_db')),
                ('Document_ver2', models.FileField(upload_to='files_db')),
            ],
        ),
    ]
