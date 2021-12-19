from MealApp.views import RateViewSet, MealViewSet
from rest_framework import routers

ROUTER = routers.DefaultRouter()

ROUTER.register('Rate', RateViewSet)
ROUTER.register('Meal', MealViewSet)
