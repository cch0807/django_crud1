from django.db import models
from django.db.models.deletion import CASCADE

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


class Drinks(models.Model):
  korean_name = models.CharField(max_length= 45)
  english_name = models.CharField(max_length=45)
  description = models.TextField()
  category = models.ForeignKey('Categories', on_delete=models.CASCADE)

  class Meta:
    db_table = 'drinks'

class Allergy_drink(models.Model):
  drink = models.ForeignKey('Drinks',on_delete= models.CASCADE)

  class Meta:
    db_table = 'allergy_drink'
  
class Allergy_join(models.Model):
  allergy_drink = models.ForeignKey('Allergy_drink', on_delete= models.CASCADE)
  allergy = models.ForeignKey('Allergy', on_delete=models.CASCADE)

  class Meta:
    db_table = 'allergy_join'

class Allergy(models.Model):
  name = models.CharField(max_length=45)

  class Meta:
    db_table = 'allergy'



class Nutritions(models.Model):
  one_serving_kca = models.DecimalField(max_digits=10, decimal_places= 2, null=True)
  sodium_mg = models.DecimalField(max_digits=10, decimal_places=2, null=True)
  saturated_fat_g = models.DecimalField(max_digits= 10, decimal_places=2, null= True)
  sugars_g = models.DecimalField(max_digits= 10, decimal_places=2, null= True)
  protein_g = models.DecimalField(max_digits= 10, decimal_places=2, null= True)
  caffeine_mg = models.DecimalField(max_digits= 10, decimal_places=2, null= True)
  drink = models.ForeignKey('Drinks', on_delete=models.CASCADE, null=True)
  size = models.ForeignKey('Sizes', on_delete=CASCADE, null=True)

  class Meta:
    db_table = 'nutritions'

class Sizes(models.Model):
  name = models.CharField(max_length=45)
  size_ml = models.CharField(max_length=45, null=True)
  size_fluid_ounce = models.CharField(max_length=45, null=True)

  class Meta:
    db_table = 'sizes'