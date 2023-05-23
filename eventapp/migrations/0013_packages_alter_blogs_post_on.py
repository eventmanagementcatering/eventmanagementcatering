# Generated by Django 4.1.6 on 2023-04-06 04:57

import datetime
from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0012_alter_menu_items'),
    ]

    operations = [
        migrations.CreateModel(
            name='packages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('eventid', models.CharField(max_length=100)),
                ('description', tinymce.models.HTMLField()),
                ('startingprice', models.CharField(max_length=100)),
                ('Numberofguest', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='blogs',
            name='post_on',
            field=models.DateField(default=datetime.date(2023, 4, 6)),
        ),
    ]
