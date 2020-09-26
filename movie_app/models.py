from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    # movie_set
    # movie_set

class Movie(models.Model):
    title = models.CharField(max_length=128)
    director = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='directed_by')
    # screen_play = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='screen_played_by', null=True)

    starring = models.ManyToManyField(Person, related_name='played_in', through="MoviePerson")

class MoviePerson(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    role = models.CharField(max_length=128)
    salary = models.DecimalField(max_digits=10, decimal_places=2)