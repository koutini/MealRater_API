from rest_framework import serializers
from .models import Rate, Meal


class MealSerializer(serializers.ModelSerializer):

    class Meta :
        model = Meal
        fields = ('title', 'discription','number_of_rating', 'average_rating')
        read_only_fields = ('number_of_rating', 'average_rating' )


class RateMealSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rate
        fields = ['user', 'stars', 'meal']
        read_only_fields  = ['id' ,'unique_id', 'meal']

