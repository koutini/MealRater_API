from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from MealApp.urls import ROUTER

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(ROUTER.urls))
]
