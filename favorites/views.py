from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from favorites.models import FavouriteProduct
from account.models import Account
from products.models import Product


@login_required(login_url="/login/")
def favorites_page(request):
    current_user = Account.objects.get(pk=request.user.id)
    favorites = FavouriteProduct.objects.filter(user=current_user)

    context = {"userid": current_user, "favorites": favorites}
    return render(request, "favorites.html", context)


@login_required(login_url="/login/")
def save_favorite(request, productid):
    current_user = Account.objects.get(pk=request.user.id)
    product = Product.objects.get(pk=productid)
    try:
        fav = FavouriteProduct.objects.get(user=current_user, product=product)
    except FavouriteProduct.DoesNotExist:
        fav = None

    if fav is not None:
        fav.delete()
    else:
        FavouriteProduct.objects.create(user=current_user, product=product)

    return HttpResponseRedirect(request.META["HTTP_REFERER"])
