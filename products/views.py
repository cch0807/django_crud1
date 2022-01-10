from django.http import JsonResponse
from django.views import View
from products.models import Menu, Categories, Drinks
import json

class ProductView(View):
  def post(self, request): #핸들러 메서드
    # data = request.body
    # print(data) # -> json data type 
    data = json.loads(request.body) #python dictionary type

    menu = Menu.objects.create(name = data["menu"])

    category = Categories.objects.create(
      name = data["category"], 
      menu_id = menu.id
    )

    drinks = Drinks.objects.create(
      korean_name = data["drinks"],
      english_name = 'yooooo',
      category_id = category.id
    )
    menus = Menu.objects.filter(name = data["names"])

    return JsonResponse({"message" : "SUCCESS"}, status=201)# 데이터 생성됬을땐 status 201사용

  def get(self, request):
    drinks = Drinks.objects.all()
    result = []
    for drink in drinks:
      result.append(
        {
          "korean_name" : drink.korean_name,
          "english_name" : drink.english_name,
          "description" : drink.description,
          "category": drink.category.name
        }
      )
    print(f"result objects :: {result}")
    return JsonResponse({"drinks": result}, status=200)

  # def delete(self, request):
  #   data = json.loads(request.body)
  #   drinks = Drinks.objects.all()
  #   print(f"{drinks}")
  #   # print(name = data["name"])
  #   # menu = Menu.objects.filter(name = data["name"]).delete()

  #   return JsonResponse({"message": "SUCCESS"}, status=201)
  # def patch

  # def put
