from django.shortcuts import render


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