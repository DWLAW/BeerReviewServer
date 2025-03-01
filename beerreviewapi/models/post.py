from django.db import models

class Post(models.Model):
    beername = models.CharField(max_length=50)
    brewery = models.CharField(max_length=50)
    review = models.CharField(max_length=500)
    rating = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    brewery = models.ForeignKey("Brewery", on_delete=models.CASCADE)
    beer_type = models.ForeignKey("BeerType", on_delete=models.CASCADE)
    tags = models.ManyToManyField("Tag", through="PostTag")
    class Meta:
        ordering = ['-created_on']
        verbose_name = ("post")
        verbose_name_plural = ("posts")
