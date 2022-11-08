
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=60, null=False, blank=False)

    def __str__(self):
        return self.name





class Product(models.Model):
    title = models.CharField(max_length=120, null=False, blank=False)
    image = models.ImageField(upload_to="products")
    price = models.IntegerField(null=True, blank=True)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)


    def __str__(self):
        return self.title



