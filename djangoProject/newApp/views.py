from django.shortcuts import render
from .models import Vegetable, Fruit, Plant

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
    search_form = SearchPlantForm(request.GET)
    if search_form.is_valid():
        data = search_form.cleaned_data
        query = data["query"]
        seasonfield = data["seasonfield"]
        sunfield = data["sunfield"]
        waterfield = data["waterfield"]
        soilfield = data["soilfield"]


        plants = search_plants( query, soilfield=soilfield , sunfield=sunfield)
        fruits = search_fruits( query, soilfield=soilfield , sunfield=sunfield)
        vegetables = search_vegetables( query, soilfield=soilfield , sunfield=sunfield)

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
        return "There are no plants with those specific requirements in this database"

def search_plants(
    query: str,
    seasonfield: Optional[str] = None,
    sunfield: Optional[str] = None,
    waterfield = Optional[str] = None,
    soilfield: Optional[str] = None,
        ) -> List[Plant]:

    if sortfield == "entered_at":
        plants = Plant.objects.all().order_by(
            sortorder + sortfield
        ) 
    else:
        plants = Plant.objects.all()

    results = plants.filter(soilfield=Plant.soil).filter(sunfield=Plant.sun)

    return results


def search_fruits(
    query: str,
    seasonfield: Optional[str] = None,
    sunfield: Optional[str] = None,
    waterfield = Optional[str] = None,
    soilfield: Optional[str] = None,

) -> List[Fruit]:

    # if soilfield == "entered_at":
    #     fruit = Fruit.objects.all().order_by(
    #         sortorder + sortfield
    #     )
    # else:
    fruit = Fruit.objects.all()

    results = fruit.filter(soilfield=Fruit.soil).filter(sunfield=Fruit.sun)

    return results


def search_vegetables(
    query: str,
    soilfield: Optional[str] = None,
    sunfield: Optional[str] = None,
) -> List[Vegetable]:

    if sortfield == "entered_at":
        vegetables = Vegetable.objects.all().order_by(
            sortorder + sortfield
        ) 
    else:
        vegetables = Vegetable.objects.all()

    results = vegetables.filter(soilfield=Vegetable.soil).filter(sunfield=Vegetable.sun)

    return results

