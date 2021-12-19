from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from .models import Rate, Meal, Profile
from rest_auth.registration.serializers import RegisterSerializer as RootRegSerializer

UserModel = get_user_model()


class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ('title', 'description', 'number_of_rating', 'average_rating')
        read_only_fields = ('number_of_rating', 'average_rating')


class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('pk', 'username', 'email', 'first_name', 'last_name')
        read_only_fields = ('email', 'username')


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('phone_number', 'date_of_birth', 'description', 'cin')
        read_only_fields = ('user',)


class UserSerializer(UserDetailsSerializer):
    """
    Add attributes in User detail serializer
    """
    # profile = SerializerMethodField()
    profile = SerializerMethodField()

    def __init__(self, instance, *args, **kwargs):
        """
        initialize update user  with profile fields.
        """
        super(UserSerializer, self).__init__(instance, *args, **kwargs)
        try:
            if self.context['request'].method in ['PUT']:
                self.fields['profile'] = ProfileSerializer()
        except KeyError:
            pass

    def get_profile(self, instance):
        """
        method to get profile according to the user.
        """
        if instance.profile:
            serializer = ProfileSerializer
            return serializer(Profile.objects.get(user=instance), read_only=True).data
        return []

    def update(self, instance, validated_data):
        validated_profile = validated_data.pop('profile')
        instance = super(UserSerializer, self).update(instance, validated_data)
        if hasattr(instance, 'profile'):
            for field, value in validated_profile.items():
                setattr(instance.profile, field, value)
            instance.profile.save()
        return instance

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + ('profile',)


class RateMealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = ['user', 'stars', 'meal']
        read_only_fields = ['id', 'unique_id', 'meal']


class RegisterSerializer(RootRegSerializer):
    """
    Gives custom serializer for user registration.
    """
    first_name = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    last_name = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    profile = ProfileSerializer()

    def get_cleaned_data(self):
        """Return cleaned data."""
        res = super(RegisterSerializer, self).get_cleaned_data()
        res.update(phone_number=self.validated_data.get('profile', {}).get('phone_number', ''),
                   date_of_birth=self.validated_data.get('profile', {}).get('date_of_birth', ''),
                   cin=self.validated_data.get('profile', {}).get('cin', ''),
                   description=self.validated_data.get('profile', {}).get('description', ''),
                   first_name=self.validated_data.get('first_name', ''),
                   last_name=self.validated_data.get('last_name', ''),
                   )
        return res

    class Meta:
        read_only_fields = ('user',)
