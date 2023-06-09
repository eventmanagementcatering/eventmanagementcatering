# Generated by Django 4.1.6 on 2023-03-17 05:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0003_decoration_events_faqs_menu_alter_blogs_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='choice',
        ),
        migrations.AlterField(
            model_name='blogs',
            name='post_on',
            field=models.DateField(default=datetime.date(2023, 3, 17)),
        ),
        migrations.AlterField(
            model_name='menu',
            name='heading',
            field=models.CharField(choices=[('Drinks', 'Drinks'), ('Starters', 'Starters'), ('Soups', 'Soups'), ('Sandwiches', 'sandwiches'), ('salads', 'salads'), ('chats', 'chats'), ('Rotis', 'Rotis'), ('Rices', 'Rices'), ('Main course', 'Main course'), ('Desserts', 'Desserts')], max_length=100),
        ),
    ]
