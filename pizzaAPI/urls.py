from django.urls import path
from .views import PizzaAPI, OrderPizzaAPIView

urlpatterns = [
    path('pizza/', PizzaAPI.as_view()),
    path('order/', OrderPizzaAPIView.as_view())
]

