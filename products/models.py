from django.db import models

# Create your models here.

class Menu(models.Model):
  name = models.CharField(max_length=45)

  class Meta:
    db_table = 'menu'

class Categories(models.Model):
  name = models.CharField(max_length=45)
  menu = models.ForeignKey('Menu', on_delete= models.CASCADE)

  class Meta:
    db_table = 'categories'

