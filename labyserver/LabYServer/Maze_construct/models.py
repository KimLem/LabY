from django.db import models


class Labyrintizer(models.Model):
    name = models.CharField(max_length=16)
    rows = models.IntegerField(max_length=3)
    columns = models.IntegerField(max_length=3)

    def __str__(self) -> str:
        return self.name
