from django.urls import path
from . import views
from Maze_construct.views import labyrinth, getLabyrinth


urlpatterns = [
    path('', views.index, name='index'),
    path('labyrinth/', labyrinth),
    path('labyrinth/json/', getLabyrinth),
]
