from rest_framework import viewsets, mixins
from .models import Meal, Rate, Profile
from .serializers import MealSerializer, RateMealSerializer, ProfileSerializer, UserSerializer
from rest_framework.decorators import action
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status


class RateViewSet(viewsets.ReadOnlyModelViewSet):
    """
       API endpoint that allows Ratinig to be viewed.
    """

    queryset = Rate.objects.all()
    serializer_class = RateMealSerializer


class MealViewSet(viewsets.ModelViewSet):
    """
       API endpoint that allows Meals to be viewed and edited.
    """

    queryset = Meal.objects.all()
    serializer_class = MealSerializer

    @action(methods=['POST'], detail=True, serializer_class=RateMealSerializer)
    def rate_meal(self, request, pk=None):
        instance = self.get_object()
        serializer = RateMealSerializer(data=request.data)
        if serializer.is_valid():
            Rate.objects.update_or_create(user=User(serializer.data.get('user')),
                                          meal=instance,
                                          defaults={'user': User(serializer.data.get('user')),
                                                    'meal': instance,
                                                    'stars': serializer.data.get('stars')})
            return Response({'status': 'done'}, status=status.HTTP_200_OK)
        return Response({'status': 'invalid data'}, status=status.HTTP_400_BAD_REQUEST)


