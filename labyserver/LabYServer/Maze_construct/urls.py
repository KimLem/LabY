from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.labyrinth, name='labyrinth'),
    path('/json', views.getLabyrinth, name='getLabyrinth'),

]
