from django.urls import path
from .views import ProductView
urlpatterns = [
  path('', ProductView.as_view()),
  # path('/<int:products_id>', ProductView),
  # path('/<int:products_id>/review', ProductView),
]