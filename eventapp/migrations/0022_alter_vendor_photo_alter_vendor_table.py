# Generated by Django 4.1.6 on 2023-04-22 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0021_alter_blogs_post_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='photo',
            field=models.ImageField(default='', upload_to='Vendor/'),
        ),
        migrations.AlterModelTable(
            name='vendor',
            table='Vendor',
        ),
    ]