# Generated by Django 4.1.6 on 2023-03-30 05:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0005_alter_blogs_post_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='decoration',
            name='price',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='post_on',
            field=models.DateField(default=datetime.date(2023, 3, 30)),
        ),
    ]
