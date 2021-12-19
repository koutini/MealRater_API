from django.contrib import admin
from .models import Meal, Rate, Profile


class MealAdmin(admin.ModelAdmin):
    """Define the Meal in the admin side."""
    list_display = ['unique_id', 'title', 'discription']
    list_filter = ['title', 'discription'] 
    search_fields  = ['title']
    

class RateAdmin(admin.ModelAdmin):
    """Define the rate in the admin side."""
    list_display = ['unique_id', 'meal', 'user' , 'stars']
    list_filter = ['meal', 'user']


class ProfileAdmin(admin.ModelAdmin):
    """Define the profile ine the admin side."""
    list_display = ['user', 'phone_number', 'cin', 'description']
    list_filter = ['phone_number', 'user', 'cin']


admin.site.register(Meal, MealAdmin) 
admin.site.register(Rate, RateAdmin)
admin.site.register(Profile, ProfileAdmin)
