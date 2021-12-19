from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from MealApp.urls import ROUTER

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(ROUTER.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path("api/v1/rest-auth/", include('rest_auth.urls')),
    path("api/v1/rest-auth/registration/", include('rest_auth.registration.urls')),

]
