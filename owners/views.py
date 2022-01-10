from django.views import View
from django.http import JsonResponse
from owners.models import Owners, Dogs
import json

class OwnerView(View):
  def post(self, request):
    # data = request.body # json obejects
    data = json.loads(request.body) #python dictionary
    owners = Owners.objects.create(
      name = data["name"],
      email = data["email"], 
      age = data["age"]
    )
    return JsonResponse({"message" : "SUCCESS"}, status= 201)

  def get(self, request):
    owners = Owners.objects.all()
    result = []
    for owner in owners:
      dog = [
        {"이름" : dog.name} for dog in Dogs.objects.filter(owner_id = owner.id)
      ]
      result.append(
        {
        "name": owner.name,
        "email": owner.email,
        "age": owner.age,
        "dog_name": dog
        }
      )
    return JsonResponse({"owners": result},status=200)

class DogView(View):
  def post(self, request):
    data = json.loads(request.body)
    dogs = Dogs.objects.create(
      name = data["name"],
      age = data["age"],
      owner_id = data["owner_id"],
    )
    return JsonResponse({"message" : "SUCCESS"}, status=201)

  def get(self, request):
    dogs = Dogs.objects.all()
    result = []
    for dog in dogs:
      result.append(
        {
          "name": dog.name,
          "age": dog.age,
          "owner_name": dog.owner.name,
        }
      )
    return JsonResponse({"dogs": result}, status=200)
