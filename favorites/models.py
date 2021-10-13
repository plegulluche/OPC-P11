from django.db import models
from account.models import Account
from products.models import Surrogate

class UsersFavorites(models.Model):
    userfav = models.ForeignKey(
        "Account",
        on_delete=models.CASCADE,
    )
    surrogatefav = models.ForeignKey(
        "Surrogate",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'this is the favorites of  {self.userfav.username}'