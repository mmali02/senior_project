from django.shortcuts import render
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


# def search(request):
#     search_form = SearchPlantForm(request.GET)
#     if search_form.is_valid():
#         data = search_form.cleaned_data
#         query = data["query"]
#         seasonfield = data["seasonfield"]
#         sunfield = data["sunfield"]
#         waterfield = data["waterfield"]
#         soilfield = data["soilfield"]
#
#
#         plants = search_plants( query, seasonfield=seasonfield,sunfield=sunfield, waterfield=waterfield, soilfield=soilfield )
#         fruits = search_fruits( query, seasonfield=seasonfield,sunfield=sunfield, waterfield=waterfield, soilfield=soilfield )
#         vegetables = search_vegetables( query, seasonfield=seasonfield,sunfield=sunfield, waterfield=waterfield, soilfield=soilfield )
#
#         return render(
#             request,
#             "garden/index.html",
#             {
#                 "query": query,
#                 "plants": plants,
#                 "fruits": fruits,
#                 "vegetables": vegetables
#             },
#         )
#     else:
#         return "There are no plants with those specific requirements in this database"


def search(request):
    search_form = SearchPlantForm(request.GET)
    if search_form.is_valid():
        data = search_form.cleaned_data
        query = data["query"]
        seasonfield = data["seasonfield"]
        sunfield = data["sun"]
        water = data["waterfield"]
        soil = data["soilfield"]

        plants, fruits, vegetables = search_plants(query, season, sun, water, soil)

        return render(
            request,
            "garden/index.html",
            {
                "query": query,
                "plants": plants,
                "fruits": fruits,
                "vegetables": vegetables
            },
        )
    else:
        return render(request, "error_page.html", {"error": "Invalid form data"})


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

    if seasonfield:
        plants = plants.filter(seasonfield=seasonfield)
        fruits = fruits.filter(seasonfield=seasonfield)
        vegetables = vegetables.filter(seasonfield=seasonfield)

    if sunfield:
        plants = plants.filter(sunfield=sunfield)
        fruits = fruits.filter(sunfield=sunfield)
        vegetables = vegetables.filter(sunfield=sunfield)

    if waterfield:
        plants = plants.filter(waterfield=waterfield)
        fruits = fruits.filter(waterfield=waterfield)
        vegetables = vegetables.filter(waterfield=waterfield)

    if soilfield:
        plants = plants.filter(soilfield=soilfield)
        fruits = fruits.filter(soilfield=soilfield)
        vegetables = vegetables.filter(soilfield=soilfield)

    return plants, fruits, vegetables


# def search_plants(
#     query: str,
#     seasonfield: Optional[str] = None,
#     sunfield: Optional[str] = None,
#     waterfield = Optional[str] = None,
#     soilfield: Optional[str] = None,
#         ) -> (List[Plant], List[Fruit], List[Vegetable]):
#
#     if sortfield == "entered_at":
#         plants = Plant.objects.all().order_by(
#             sortorder + sortfield
#         )
#         fruits = Fruit.objects.all().order_by(
#             sort
#         )
#     else:
#         plants = Plant.objects.all()
#         fruits = Fruit.objects.all()
#         vegetables = Vegetable.objects.all()
#
#     results = plants.filter(seasonfield=Plant.season).filter(sunfield=Plant.sun).filter(waterfield=Plant.water).filter(soilfield=Plant.soil)
#     results1 = fruits.filter(seasonfield=Fruit.season).filter(sunfield=Fruit.sun).filter(waterfield=Fruit.water).filter(soilfield=Fruit.soil)
#     results2 = vegetables.filter(seasonfield=Vegetable.season).filter(sunfield=Vegetable.sun).filter(waterfield=Vegetable.water).filter(soilfield=Vegetable.soil)
#     return results, results1, results2

#
# def search_fruits(
#     query: str,
#     seasonfield: Optional[str] = None,
#     sunfield: Optional[str] = None,
#     waterfield = Optional[str] = None,
#     soilfield: Optional[str] = None,
#
# ) -> List[Fruit]:
#
#     # if soilfield == "entered_at":
#     #     fruit = Fruit.objects.all().order_by(
#     #         sortorder + sortfield
#     #     )
#     # else:
#     fruit = Fruit.objects.all()
#
#     results = fruit.filter(soilfield=Fruit.soil).filter(sunfield=Fruit.sun)
#
#     return results
#
#
# def search_vegetables(
#     query: str,
#     soilfield: Optional[str] = None,
#     sunfield: Optional[str] = None,
# ) -> List[Vegetable]:
#
#     if sortfield == "entered_at":
#         vegetables = Vegetable.objects.all().order_by(
#             sortorder + sortfield
#         )
#     else:
#         vegetables = Vegetable.objects.all()
#
#     results = vegetables.filter(soilfield=Vegetable.soil).filter(sunfield=Vegetable.sun)
#
#     return results
#
