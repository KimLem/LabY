from django.urls import path
from . import views
from Maze_construct.views import labyrinth


urlpatterns = [
    path('', views.index, name='index'),
    path('labyrinth/', labyrinth),
    ]