from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Place(models.Model):
    name = models.CharField(max_length=150)
    category = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    lat = models.FloatField(
        validators=[MinValueValidator(-90), MaxValueValidator(90)]
    )
    lng = models.FloatField(
        validators=[MinValueValidator(-180), MaxValueValidator(180)]
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
