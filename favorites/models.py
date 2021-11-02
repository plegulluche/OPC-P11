from django.db import models

from products.models import Products
from account.models import Account

class FavouriteProduct(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='product')
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='user')
    is_favourite = models.BooleanField(default=True)

    def __str__(self):
        return f'product {self.product.productName} {"marked favourite"} by {self.user.username}'