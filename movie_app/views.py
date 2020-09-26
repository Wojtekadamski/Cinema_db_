from itertools import repeat

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from movie_app.models import Person, Movie, Genre


def movie_view(request):
    persons = Person.objects.all()
    genres = Genre.objects.all()
    movies = Movie.objects.all()
    content = {'persons': persons, 'movies': movies, 'genres': genres}
    if request.method == 'GET':
        return render(request, "add_movie.html", content)

    title = request.POST['title']
    director_id = request.POST['director']
    screen_play_id = request.POST['screen_play']
    genre_id = request.POST['genre']
    director = Person.objects.get(pk=director_id)
    screen_play = Person.objects.get(pk=screen_play_id)

    year = request.POST['year']
    rating = request.POST['rating']
    starring_id = request.POST['starring']

    movie = Movie.objects.create(title=title, director=director, screen_play=screen_play,  year=year, rating=rating)
    movie.starring.set(starring_id)
    movie.genre.set(genre_id)
    return render(request, "add_movie.html", content)


def person_view(request):
    if request.method == 'POST':
        imie = request.POST['first_name']
        nazwisko = request.POST['last_name']
        Person.objects.create(first_name=imie, last_name=nazwisko)
    persons = Person.objects.all()
    return render(request, 'add_person.html', {'persons': persons})


def genre_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        genres = Genre.objects.all()
        Genre.objects.create(name=name)
    genres = Genre.objects.all()
    return render(request, 'add_genre.html', {'genres': genres})


def movie_detail(request, id):
    persons = Person.objects.all()
    genres = Genre.objects.all()
    movies = Movie.objects.all()
    movie = Movie.objects.get(pk = id)
    content = {'persons': persons, 'movies': movies, 'genres': genres, 'movie':movie}
    return render(request, 'detail_view.html', content)

