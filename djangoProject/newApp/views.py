from django.shortcuts import render
from django.http import HttpResponse
from typing import Optional, List
from .models import Vegetable, Fruit, Plant
from .forms import SearchPlantForm


# Create your views here.
# Defining a view for inside index.html, (turning a request into a response)
def index(request):
    return render(request, "newApp/index.html", {})

# Defining a view for inside garden.html, (turning a request into a response)
def garden(request):
    return render(request, "newApp/garden.html", {})

def references(request):
    return render(request, "newApp/references.html", {})

def external_reference(request, url):
    # Logic to handle the external reference URL
    return render(request, 'external_reference.html', {'external_url': url})

def plant_info_base(request):
    fruit_list = Fruit.objects.all()
    veg_list = Vegetable.objects.all()
    plant_list = Plant.objects.all()
    return render(request, 'newApp/plant_info_base.html', {'fruit_list': fruit_list, 'veg_list': veg_list, 'plant_list': plant_list})



def search(request):
    query_param = request.GET.get('query')
    seasonfield_param = request.GET.get('seasonfield')
    sunfield_param = request.GET.get('sunfield')
    waterfield_param = request.GET.get('waterfield')
    soilfield_param = request.GET.get('soilfield')

    if request.method == 'GET':
        search_form = SearchPlantForm(request.GET)
        if search_form.is_valid():
            data = search_form.cleaned_data
            query = data.get("query", "")
            season = data.get("seasonfield", "")
            sun = data.get("sunfield", "")
            water = data.get("waterfield", "")
            soil = data.get("soilfield", "")

            plants, fruits, vegetables = search_plants(query, season, sun, water, soil)


            # Check if any items are found after filtering
            if not (plants or fruits or vegetables):
                return render(request, "newApp/plant_info_base.html",
                              {"error_message": "We're sorry, there are no plants matching your selected filters."})

            return render(
                request,
                "newApp/plant_info_base.html",
                {
                    "query": query,
                    "plant_list": plants,
                    "fruit_list": fruits,
                    "veg_list": vegetables
                },
            )
        else:
            # If the form is not valid, render the search form with errors
            return render(request, 'search.html', {'search_form': search_form, 'error_message': 'Invalid form data'})
    else:
        # Handle other HTTP methods if needed
        return HttpResponse(status=405)  # Method Not Allowed




def search_plants(
    query: str,
    seasonfield: Optional[str] = None,
    sunfield: Optional[str] = None,
    waterfield: Optional[str] = None,
    soilfield: Optional[str] = None,
) -> (List[Plant], List[Fruit], List[Vegetable]):

    plants = Plant.objects.all()
    fruits = Fruit.objects.all()
    vegetables = Vegetable.objects.all()

    if query:
        plants = plants.filter(name__icontains=query)
        fruits = fruits.filter(name__icontains=query)
        vegetables = vegetables.filter(name__icontains=query)

    if seasonfield and seasonfield != 'Any':
        plants = plants.filter(season=seasonfield)
        fruits = fruits.filter(season=seasonfield)
        vegetables = vegetables.filter(season=seasonfield)

    if sunfield and sunfield != 'Any':
        plants = plants.filter(sun=sunfield)
        fruits = fruits.filter(sun=sunfield)
        vegetables = vegetables.filter(sun=sunfield)

    if waterfield and waterfield != 'Any':
        plants = plants.filter(water=waterfield)
        fruits = fruits.filter(water=waterfield)
        vegetables = vegetables.filter(water=waterfield)

    if soilfield and soilfield != 'Any':
        plants = plants.filter(soil=soilfield)
        fruits = fruits.filter(soil=soilfield)
        vegetables = vegetables.filter(soil=soilfield)

    return plants, fruits, vegetables


