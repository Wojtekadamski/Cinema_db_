from django.db import models


# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    # movie_set
    # movie_set
class Genre(models.Model):
    name = models.CharField(max_length=128)

class Movie(models.Model):
    title = models.CharField(max_length=128)
    director = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='directed_by')
    screen_play = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='screen_played_by', null=True)
    rating = models.IntegerField(null=True)
    starring = models.ManyToManyField(Person, related_name='played_in', through="MoviePerson")
    year = models.IntegerField( null=True)
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return f"tytuł: {self.title}\nreżyser: {self.director.first_name} {self.director.last_name}\nscenarzysta: {self.screen_play.first_name} {self.screen_play.last_name}\nocena: {self.rating}\n"


class MoviePerson(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    role = models.CharField(max_length=128, null = True)



