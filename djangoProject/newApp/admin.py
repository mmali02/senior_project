from django.contrib import admin
from .models import Vegetables
from .models import Fruits
from .models import Plants

admin.site.register(Vegetables)
admin.site.register(Fruits)
admin.site.register(Plants)
