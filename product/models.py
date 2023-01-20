from django.db import models


class Category(models.Model):
    category_id = models.IntegerField(primary_key=True)
    categorydesc = models.CharField(max_length=40)

    def __str__(self):
        return self.categorydesc


class Product(models.Model):
    name = models.CharField(max_length=30, null=True)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    img = models.ImageField(null=True, blank=True, upload_to="photos")

    def __str__(self):
        return self.name
