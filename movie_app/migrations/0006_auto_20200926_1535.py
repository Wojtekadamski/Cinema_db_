# Generated by Django 3.1.1 on 2020-09-26 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0005_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='genre',
            field=models.ManyToManyField(to='movie_app.Genre'),
        ),
        migrations.AddField(
            model_name='movie',
            name='rating',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='screen_play',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='screen_played_by', to='movie_app.person'),
        ),
        migrations.AddField(
            model_name='movie',
            name='year',
            field=models.IntegerField(null=True),
        ),
    ]