from django.urls import path
from .views import OwnerView, DogView
urlpatterns = {
  path('/owners', OwnerView.as_view()),
  path('/dogs', DogView.as_view())
}