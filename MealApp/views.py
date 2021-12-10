from rest_framework import viewsets
from rest_framework.serializers import Serializer

from MealApp.models import Meal, Rate 
from .serializers import RateSerializer , MealSerializer


class RateViewSet(viewsets.ModelViewSet): 
    queryset = Rate.objects.all() 
    serializer_class = RateSerializer
   

class MealViewSet(viewsets.ModelViewSet): 

    queryset = Meal.objects.all() 
    serializer_class = MealSerializer
   
