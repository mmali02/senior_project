from django import forms
from django.forms import ChoiceField

from .models import Plant, Fruit, Vegetable

class SearchPlantForm(forms.Form):
    query = forms.CharField(required=False)
    soilfield = ChoiceField(
        choices=[
            ("", "Soil Type"),
            ("Clay soil", "Clay soil"),
            ("Loam soil", "Loam soil"),
            ("Sandy soil", "Sandy soil"),
        ],
    )
        sunfield = ChoiceField(
            choices=[
                ("", "Soil Type"),
                ("Clay soil", "Clay soil"),
                ("Loam soil", "Loam soil"),
                ("Sandy soil", "Sandy soil"),
            ],
        label="",
        required=False,
    )
