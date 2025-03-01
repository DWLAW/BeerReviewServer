from django.db import models


class Brewery(models.Model):
    name = models.CharField(max_length=50)
    locals = models.CharField(max_length=50)
