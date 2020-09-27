from itertools import repeat

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from movie_app.models import Person, Movie, Genre, Publisher


def movie_view(request):
    persons = Person.objects.all()
    genres = Genre.objects.all()
    movies = Movie.objects.all()
    producers = Publisher.objects.all()
    content = {'persons': persons, 'movies': movies, 'genres': genres, 'producers': producers}
    if request.method == 'GET':
        return render(request, "add_movie.html", content)

    title = request.POST['title']
    director_id = request.POST['director']
    screen_play_id = request.POST['screen_play']
    producer_id = request.POST.get('producer_id')
    genre_id = request.POST['genre']
    director = Person.objects.get(pk=director_id)
    screen_play = Person.objects.get(pk=screen_play_id)
    producer = Publisher.objects.get(pk=producer_id)

    year = request.POST['year']
    rating = request.POST['rating']
    starring_id = request.POST['starring']

    movie = Movie.objects.create(title=title, director=director, screen_play=screen_play, year=year, rating=rating,
                                 producer=producer)
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


class MovieDataView(View):
    def get(self, request, id):
        persons = Person.objects.all()
        genres = Genre.objects.all()
        movies = Movie.objects.all()
        movie = Movie.objects.get(pk=id)
        content = {'persons': persons, 'movies': movies, 'genres': genres, 'movie': movie}
        return render(request, 'detail_view.html', content)

    def post(self, request, id):
        title = request.POST.get('title')
        year = request.POST.get('year')
        rating = request.POST.get('rating')
        starring = request.POST.getlist('starring')
        genre = request.POST.getlist('genre')
        director_id = request.POST.get('director_id')
        screen_play_id = request.POST.get('screen_play_id')
        producer_id = request.POST.get('producer_id')
        movie = Movie.objects.get(pk=id)
        movie.title = title
        movie.year = year
        movie.rating = rating
        movie.starring = starring
        movie.genre.set(genre)
        movie.director.id = director_id
        movie.screen_play.id = screen_play_id
        movie.director.id = director_id
        movie.producer.id = producer_id

        movie.save()
        return redirect(f'/detail_view/{id}/')


class AddPublisher(View):
    def get(self, request, id=None):
        publishers = Publisher.objects.all()
        name = request.GET.get('name')
        if name is not None:
            publishers = publishers.filter(name__icontains=name)
        if id is not None:
            publisher = Publisher.objects.get(pk=id)
            content = {'publisher': publisher, 'publishers': publishers}
            return render(request, 'add_publisher.html', content)

        return render(request, 'add_publisher.html', {'publishers': publishers})

    def post(self, request, id=None):
        if id is not None:
            name = request.POST.get('name')
            address = request.POST.get('address')
            publisher = Publisher.objects.get(pk=id)
            publisher.name = name
            publisher.address = address
            publisher.save()
            publishers = Publisher.objects.all()
            return redirect(f'/publisher/')
        name = request.POST.get('name')
        address = request.POST.get('address')
        Publisher.objects.create(name=name, address=address)
        publishers = Publisher.objects.all()
        return render(request, 'add_publisher.html', {'publishers': publishers})
