from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Actors(models.Model):
  first_name = models.CharField(max_length=45)
  last_name = models.CharField(max_length=45)
  date_of_birth = models.DateField()
  movie = models.ManyToManyField('Movies', through='Actors_movies')

  class Meta:
    db_table = 'actors'


class Actors_movies(models.Model):
  actor = models.ForeignKey('Actors',on_delete=CASCADE)
  movie = models.ForeignKey('Movies', on_delete=CASCADE)

  class Meta:
    db_table = 'actors_movies'


class Movies(models.Model):
  title = models.CharField(max_length=45)
  release_date = models.DateField()
  running_time = models.IntegerField()

  class Meta:
    db_table = 'movies'