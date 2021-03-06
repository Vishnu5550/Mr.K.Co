# Generated by Django 3.2.4 on 2021-06-28 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sampleapp', '0017_cars'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=54)),
                ('Documents', models.FileField(blank=True, upload_to='files_db')),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('images', models.FileField(blank=True, upload_to='pics')),
            ],
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='Document_per1',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='Document_per2',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='Document_ver1',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='Document_ver2',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='Image_1',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='Image_2',
        ),
    ]
