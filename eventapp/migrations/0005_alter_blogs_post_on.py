# Generated by Django 4.1.6 on 2023-03-18 04:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0004_remove_menu_choice_alter_blogs_post_on_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='post_on',
            field=models.DateField(default=datetime.date(2023, 3, 18)),
        ),
    ]