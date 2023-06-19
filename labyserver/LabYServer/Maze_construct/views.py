from django.shortcuts import render
from Maze_Generator import Labyrinth


def labyrinth(request):

    mazerMaker = Labyrinth.Labyrinth(10, 10)
    [right_walls, bot_walls] = mazerMaker.serialize()
    mazer = mazerMaker.serializeToJSON()

    return render(request, 'Maze_construct/labyrinth.html', {'mazer': mazer,
                                                             'bot_walls': bot_walls})


def getLabyrinth(request):

    rows = 10
    columns = 10

    # if request.method == "GET":

    #     # mazer1 = {"__Labyrinth__": True, "name": "", "rows": 10, "columns": 10,
    #     #           "walls": [{"__Wall__": True, "Type": "vertical", "X": 0, "Y": 0}]
    #     #           }
    #     # mazer1 = {"govno": True}

    mazer1 = Labyrinth.Labyrinth(rows, columns).serializeToJSON()
    #     # mazer1 = Labyrinth.Labyrinth._encodeLabyrinth(
    #     #     Labyrinth.Labyrinth(rows, columns))
    #     print(mazer1)

    return render(request, 'Maze_construct/labyrinth.html', mazer1)
    # return render(request, 'Maze_construct/labyrinth.html', {"rows": rows, "columns": columns})
