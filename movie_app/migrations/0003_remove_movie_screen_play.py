# Generated by Django 3.1.1 on 2020-09-26 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0002_auto_20200926_0845'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='screen_play',
        ),
    ]
