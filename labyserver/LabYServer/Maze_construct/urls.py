from django.urls import path
from . import views

urlpatterns = [
    path('', views.labyrinth, name='labyrinth'),
    path('getNewLabyrinth', views.getNewLabyrinth, name='getNewLabyrinth'),
    path('setLParams', views.setLParams, name='setLParams'),


]
