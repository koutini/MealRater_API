from django.core import validators
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import  MaxValueValidator, MinValueValidator
import uuid


class Meal(models.Model): 
    """ Define the meal model."""
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=100) 
    discription = models.TextField(max_length=500) 

    def __str__(self): 
        """
        Override this method to format meal object.'
        """
        return self.title  

class Rate(models.Model): 
    """ Define the rate model. """
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    
    class  Meta:
       unique_together = ('user', 'meal', )



    def __str__(self): 
        """
        Override this method to format rate object.'
        """
        return self.meal