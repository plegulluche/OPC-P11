from django.db import models

class Products(models.Model):
    productID = models.BigAutoField(primary_key=True)
    productName = models.CharField(max_length=400, unique=True)
    nutriScore = models.CharField(max_length=1)
    linkToIMG = models.CharField(max_length=300, unique=True)
    linkToURLOFF = models.CharField(max_length=300, unique=True)
    linkToNutriForG = models.CharField(max_length=300, unique=True)
    
    def __str__(self):
        return self.productName


class Category(models.Model):
    categoryID = models.BigAutoField(primary_key=True, default=0)
    categoryName = models.CharField(max_length=400, unique=True, default='to erase')

    def __str__(self):
        return self.categoryName


class Surrogate(models.Model):
    produit = models.ForeignKey(
        "Products",
        related_name= "surrogate_product",
        on_delete=models.CASCADE,
        )
    substitut = models.ForeignKey(
        "Products",
        related_name = "surrogate_surrogate",
        on_delete = models.CASCADE,
    )
    
    def __str__(self):
        return self.surrogate
    
class ProductsCategory(models.Model):
    category = models.ForeignKey(
        "Category",
        on_delete=models.CASCADE,
        
    )
    product = models.ForeignKey(
        "Products",
        on_delete=models.CASCADE,
    )

