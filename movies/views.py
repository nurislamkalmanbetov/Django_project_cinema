from django.shortcuts import render
from django.views.generic.base import View

from .models import Movie
# Create your views here.




class MoviesView(View):
    """Список фильмов"""
    def get(self, request):
        movies = Movie.objects.all()
        return render(request, "movies/movies.html", {"movie_list": movies}) #movie_list в темплейтах будем переберать
