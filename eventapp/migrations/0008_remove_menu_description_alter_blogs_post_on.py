# Generated by Django 4.1.6 on 2023-04-04 05:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0007_menu_description_menu_photo_alter_blogs_post_on'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='description',
        ),
        migrations.AlterField(
            model_name='blogs',
            name='post_on',
            field=models.DateField(default=datetime.date(2023, 4, 4)),
        ),
    ]