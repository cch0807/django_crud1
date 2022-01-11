from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from movies.models import Actors,Movies,Actors_movies
import json
# Create your views here.

class ActorView(View):
  def post(self, request):
    data = json.loads(request.body)
    actors = Actors.objects.create(
      first_name = data["first_name"],
      last_name = data["last_name"],
      date_of_birth = data["date_of_birth"]
    )

    return JsonResponse({"message": "SUCCESS"}, status = 201)

  def get(self, request):
    actors = Actors.objects.all()
    result = []
    for actor in actors:
      movie_list = []
      movies = actor.movie.all()
      for movie in movies:
        movie_list.append(movie.title)
      movie_information = {
        'first_name': actor.first_name,
        'last_name': actor.last_name,
        'movies': movie_list
      }
      result.append(movie_information)
    return JsonResponse({"actors": result}, status=200)

class MovieView(View):
  def post(self,request):
    data = json.loads(request.body)
    movies = Movies.objects.create(
      title = data["title"],
      release_date = data["release_date"],
      running_time = data["running_time"],
    )
    return JsonResponse({"message":"SUCCESS"}, status=201)
  
  def get(self, request):
    movies = Movies.objects.all()
    result = []
    for movie in movies:
      actors = movie.actors_set.all()
      actor_list = []
      for actor in actors:
        actor_list.append(actor.first_name + actor.last_name)
        
      result.append({
        "title": movie.title,
        "running_time": movie.running_time,
        "actor_name": actor_list
        })

    return JsonResponse({"movies": result}, status=200)


class Actor_MovieView(View):
  def post(self,request):
    data = json.loads(request.body)
    actor_movie = Actors_movies.objects.create(
      actor_id = data["actor_id"],
      movie_id = data["movie_id"],
    )

    return JsonResponse({"message": "SUCCESS"}, status=201)