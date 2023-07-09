from django.shortcuts import render
from Maze_Generator import Labyrinth
from django.http import JsonResponse
from .forms import LabyrintyzerForm
from uuid import uuid4


def labyrinth(request):

    mazerMaker = Labyrinth.Labyrinth(10, 10)
    [right_walls, bot_walls] = mazerMaker.serialize()
    mazer = mazerMaker.serializeToJSON()

    return render(request, 'Maze_construct/labyrinth.html', {'mazer': mazer,
                                                             'bot_walls': bot_walls})


def getNewLabyrinth(request):

    rows = 20
    columns = 20

    # if request.method == "GET":
    mazer1 = Labyrinth.Labyrinth._encodeLabyrinth(
        Labyrinth.Labyrinth(rows, columns))

    return JsonResponse(mazer1)


def setLParams(request):

    form = LabyrintyzerForm()

    if request.method == "POST":

        form = LabyrintyzerForm(request.POST)
        if form.is_valid():
            rows = form.cleaned_data['rows']
            columns = form.cleaned_data['columns']
            form.save()

            mazer = Labyrinth.Labyrinth._encodeLabyrinth(
                Labyrinth.Labyrinth(rows, columns))

            return JsonResponse(mazer)
        else:
            errors = form.errors.as_json()
            return JsonResponse({"errors": errors}, status=400)

    return render(request, "Maze_construct/labyrinth.html", {"form": form})

    # if request.method == "GET":
    #     mazer = Labyrinth.Labyrinth._encodeLabyrinth(
    #         Labyrinth.Labyrinth(rows, columns))
    #     return JsonResponse(mazer)
