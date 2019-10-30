from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Product(models.Model):
    title = models.CharField(max_length=200, default="")
    rating = models.DecimalField(max_digits=3, decimal_places=2, validators=[MinValueValidator(0), MaxValueValidator(5)])
    review_num = models.IntegerField(default=0)
    price = models.FloatField(default=0)
    owner = models.CharField(max_length=50, default="")
    amazon_link = models.CharField(max_length=200, default="")
    user = models.ForeignKey('auth.User', related_name='product', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title
        

