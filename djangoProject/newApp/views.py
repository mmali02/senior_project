from django.shortcuts import render


# Create your views here.
# Defining a view for inside index.html, (turning a request into a response)
def index(request):
    render(request, "newApp/index.html", {})
