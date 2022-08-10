from django.contrib import admin

from .models import Sauce, Stock, Dish

# Register your models here.
admin.site.register(Sauce)
admin.site.register(Stock)
admin.site.register(Dish)