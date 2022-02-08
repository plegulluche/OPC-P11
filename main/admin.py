from django.contrib import admin
from products.models import Nutrimage, Product, Category
from account.models import Account
from favorites.models import FavouriteProduct

# Register your models here.
admin.site.register(Nutrimage)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Account)
admin.site.register(FavouriteProduct)


class UserAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "email",
        "token",
        "email_is_active",
    )
