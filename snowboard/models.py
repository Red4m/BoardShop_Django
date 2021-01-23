from django.db import models


class Snowboard(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    description = models.TextField()
    cost = models.FloatField(default=0)
    manufacturer_country = models.CharField(max_length=50)

    def __str__(self):
        return self.name
