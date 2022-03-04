from django.urls import path
from . import views

app_name = "rendu"
urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('<int:id>', views.show, name='show'),
    path('cart/<int:id>', views.cart, name='cart'),
]
