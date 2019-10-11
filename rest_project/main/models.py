from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Product(models.Model):
    title = models.CharField(max_length=200, default="")
    prime = models.BooleanField(default=False)
    rating = models.DecimalField(max_digits=3, decimal_places=2, validators=[MinValueValidator(0), MaxValueValidator(5)])
    review_num = models.IntegerField(default=0)
    price = models.FloatField(default=0)


