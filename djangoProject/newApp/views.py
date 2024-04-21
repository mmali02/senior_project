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


# current search:
# def search(request):
#     search_form = SearchPlantForm(request.GET)
#
#     if search_form.is_valid():
#         data = search_form.cleaned_data
#         query = data["query"]
#         season = data["seasonfield"]
#         sun = data["sunfield"]
#         water = data["waterfield"]
#         soil = data["soilfield"]
#
#         plants, fruits, vegetables = search_plants(query, season, sun, water, soil)
#
#         return render(
#             request,
#             "newApp/plant_info_base.html",
#             {
#                 "query": query,
#                 "plants": plants,
#                 "fruits": fruits,
#                 "vegetables": vegetables
#             },
#         )
#     else:
#         # If the form is not valid, print an error message
#         print("Form is not valid:", search_form.errors)
#         return HttpResponse("Invalid form data")
#         # return "There are no plants with those specific requirements in this database"
#         # return render(request, "error_page.html", {"error": "Invalid form data"})


# def search(request):
#     query_param = request.GET.get('query')
#     seasonfield_param = request.GET.get('seasonfield')
#     sunfield_param = request.GET.get('sunfield')
#     waterfield_param = request.GET.get('waterfield')
#     soilfield_param = request.GET.get('soilfield')
#
#     # Print the parameters to inspect them
#     print("Query:", query_param)
#     print("Seasonfield:", seasonfield_param)
#     print("Sunfield:", sunfield_param)
#     print("Waterfield:", waterfield_param)
#     print("Soilfield:", soilfield_param)
#
#     if request.method == 'GET':
#         search_form = SearchPlantForm(request.GET)
#         if search_form.is_valid():
#             data = search_form.cleaned_data
#             query = data.get("query", "")
#             season = data.get("seasonfield", "")
#             sun = data.get("sunfield", "")
#             water = data.get("waterfield", "")
#             soil = data.get("soilfield", "")
#
#             plants, fruits, vegetables = search_plants(query, season, sun, water, soil)
#
#             return render(
#                 request,
#                 "newApp/plant_info_base.html",
#                 {
#                     "query": query,
#                     "plant_list": plants,
#                     "fruit_list": fruits,
#                     "veg_list": vegetables
#                 },
#             )
#         else:
#             # If the form is not valid, render the search form with errors
#             return render(request, 'search.html', {'search_form': search_form, 'error_message': 'Invalid form data'})
#     else:
#         # Handle other HTTP methods if needed
#         return HttpResponse(status=405)  # Method Not Allowed



def search(request):
    query_param = request.GET.get('query')
    seasonfield_param = request.GET.get('seasonfield')
    sunfield_param = request.GET.get('sunfield')
    waterfield_param = request.GET.get('waterfield')
    soilfield_param = request.GET.get('soilfield')

    # Print the parameters to inspect them
    print("Query:", query_param)
    print("Seasonfield:", seasonfield_param)
    print("Sunfield:", sunfield_param)
    print("Waterfield:", waterfield_param)
    print("Soilfield:", soilfield_param)

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

            # Print the length of each queryset for debugging
            print("Number of plants:", len(plants))
            print("Number of fruits:", len(fruits))
            print("Number of vegetables:", len(vegetables))

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

    if seasonfield and seasonfield != 'All':
        plants = plants.filter(season=seasonfield)
        fruits = fruits.filter(season=seasonfield)
        vegetables = vegetables.filter(season=seasonfield)

    if sunfield and sunfield != 'All':
        plants = plants.filter(sun=sunfield)
        fruits = fruits.filter(sun=sunfield)
        vegetables = vegetables.filter(sun=sunfield)

    if waterfield and waterfield != 'All':
        plants = plants.filter(water=waterfield)
        fruits = fruits.filter(water=waterfield)
        vegetables = vegetables.filter(water=waterfield)

    if soilfield and soilfield != 'All':
        plants = plants.filter(soil=soilfield)
        fruits = fruits.filter(soil=soilfield)
        vegetables = vegetables.filter(soil=soilfield)

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
