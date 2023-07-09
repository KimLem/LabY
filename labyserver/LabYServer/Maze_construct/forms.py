from django import forms
from .models import Labyrintizer


class LabyrintyzerForm(forms.ModelForm):
    class Meta:
        model = Labyrintizer
        fields = {'rows', 'columns'}
