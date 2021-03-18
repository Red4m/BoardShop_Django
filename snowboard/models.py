from PIL import Image
from django.db import models
import os.path


class Snowboard(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images', null=True, blank=True)
    description = models.TextField()
    cost = models.FloatField(default=0)
    manufacturer_country = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def save(self):

        if not os.path.exists(self.image.path):
            super().save()
            img = Image.open(self.image.path)
            if img.height > 325 or img.width > 155:
                output_size = (800, 400)
                img.thumbnail(output_size)
                img.save(self.image.path)
