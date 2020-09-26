from itertools import repeat

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from movie_app.models import Person, Movie


def movie_view(request):
    persons = Person.objects.all()
    if request.method == 'GET':
        return render(request, "add_movie.html", {'persons':persons})

    title = request.POST['title']
    director_id = request.POST['director']
    director = Person.objects.get(pk=director_id)
    Movie.objects.create(title=title, director=director)
    movies= Movie.objects.all()
    return render(request, "add_movie.html", {'persons': persons, 'movies':movies})


def person_view(request):
    if request.method == 'POST':
        imie = request.POST['first_name']
        nazwisko = request.POST['last_name']
        Person.objects.create(first_name=imie, last_name=nazwisko)
    persons = Person.objects.all()
    return render(request, 'add_person.html', {'persons': persons})


