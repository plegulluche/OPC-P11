from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=600, unique=True, default="to erase")

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=600)
    nutriScore = models.CharField(max_length=1)
    linkToIMG = models.CharField(max_length=600)
    linkToURLOFF = models.CharField(max_length=600)
    linkToNutriForG = models.CharField(max_length=600)
    category = models.ManyToManyField(Category)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name


class Nutrimage(models.Model):
    name = models.CharField(max_length=1)
    link = models.CharField(max_length=600)

    class Meta:
        verbose_name = "Nutriscore Image"
        verbose_name_plural = "Nutriscores Images"

    def __str__(self):
        return self.name
