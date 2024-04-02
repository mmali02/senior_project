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