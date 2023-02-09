from django.shortcuts import render
from Maze_Generator import Labyrinth


def labyrinth(request):

    mazerMaker = Labyrinth.Labyrinth(10, 10)
    [right_walls, bot_walls] = mazerMaker.serialize()

    return render(request, 'Maze_construct/labyrinth.html', {'right_walls': right_walls,
                                                             'bot_walls': bot_walls})