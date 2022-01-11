from django.db.models.base import Model
from django.urls import path
from .views import ActorView,MovieView,Actor_MovieView
urlpatterns = [
  path('/actors', ActorView.as_view()),
  path('/movies', MovieView.as_view()),
  path('/actors_movies', Actor_MovieView.as_view())
]