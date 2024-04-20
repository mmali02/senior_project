from django import forms
from django.forms import ChoiceField

from .models import Plant, Fruit, Vegetable

class SearchPlantForm(forms.Form):
    query = forms.CharField(label="Search", required=False)
    # query = forms.CharField(required=False)
    seasonfield = ChoiceField(
        choices=[
            ("", "Time of Year"),
            ("December-February", "December-February"),
            ("March-May", "March-May"),
            ("June-August", "June-August"),
            ("September-November", "September-November"),
        ],
        label="",
        required=False,
        initial=''
    )
    sunfield = ChoiceField(
        choices=[
            ("", "Sunlight"),
            ("Full sun", "Full sun"),
            ("Partial sun/shade", "Partial sun/shade"),
            ("Full shade", "Full shade"),
        ],
        label="",
        required=False,
        initial=''
    )
    waterfield = ChoiceField(
        choices=[
            ("", "Water"),
            ("Very low (every other week)", "Very low (every other week)"),
            ("Low (once per week)", "Low (once per week)"),
            ("Moderate (2 to 3 times a week)", "Moderate (2 to 3 times a week)"),
            ("High (3 to 4 times a week)", "High (3 to 4 times a week)"),
        ],
        label="",
        required=False,
        initial=''
    )
    soilfield = ChoiceField(
        choices=[
            ("", "Soil Type"),
            ("Clay soil", "Clay soil"),
            ("Loam soil", "Loam soil"),
            ("Sandy soil", "Sandy soil"),
        ],
        label="",
        required=False,
        initial=''
    )
    query = forms.CharField(label="Search", required=False)