from django.db import models

class BeerType(models.Model):

    name = models.CharField(max_length=50)
