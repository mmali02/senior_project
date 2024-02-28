from django.contrib import admin
from .models import Vegetable
from .models import Fruit
from .models import Plant

admin.site.register(Vegetable)
admin.site.register(Fruit)
admin.site.register(Plant)
