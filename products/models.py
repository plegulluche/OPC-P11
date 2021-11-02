from django.db import models


class Category(models.Model):
    categoryName = models.CharField(max_length=400, unique=True, default='to erase')

    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.categoryName
    

class Products(models.Model):
    productName = models.CharField(max_length=400, unique=True)
    nutriScore = models.CharField(max_length=1)
    linkToIMG = models.CharField(max_length=300, unique=True)
    linkToURLOFF = models.CharField(max_length=300, unique=True)
    linkToNutriForG = models.CharField(max_length=300, unique=True)
    category = models.ManyToManyField(Category)
    
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        
        
    def __str__(self):
        return self.productName 
    