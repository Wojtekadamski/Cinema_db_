# Generated by Django 3.1.1 on 2020-09-26 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0006_auto_20200926_1535'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movieperson',
            name='salary',
        ),
        migrations.AlterField(
            model_name='movieperson',
            name='role',
            field=models.CharField(max_length=128, null=True),
        ),
    ]
