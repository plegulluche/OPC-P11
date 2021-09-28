from os import name
from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    
    

