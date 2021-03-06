"""MovieDb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from movie_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_person/', views.person_view),
    path('add_movie/', views.movie_view),
path('add_genre/', views.genre_view),
path('movie_detail/<int:id>/', views.MovieDataView.as_view()),
path('publisher/', views.AddPublisher.as_view()),
path('publisher/<int:id>/', views.AddPublisher.as_view()),

]
