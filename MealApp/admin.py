from django.contrib import admin
from .models import Meal, Rate


class MealAdmin(admin.ModelAdmin):
    """Define the Meal in the admin side."""
    list_display = ['unique_id', 'title', 'discription']
    list_filter = ['title', 'discription'] 
    search_fields  = ['title']
    

     

class RateAdmin(admin.ModelAdmin):
    """Define the rate in the admin side."""
    list_display = ['unique_id', 'meal', 'user' , 'stars']
    list_filter = ['meal', 'user']


admin.site.register(Meal, MealAdmin) 
admin.site.register(Rate, RateAdmin)
