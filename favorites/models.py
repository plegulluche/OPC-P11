from django.db import models

from products.models import Product
from account.models import Account


class FavouriteProduct(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="user")
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="product"
    )
    is_favourite = models.BooleanField(default=True)

    def __str__(self):
        return (
            f'product {self.product.name} {"marked favourite"} by {self.user.username}'
        )
