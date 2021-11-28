from re import sub
from unicodedata import category
from django.shortcuts import render,redirect
from django.db.models import Q
from products.models import Product,Category,Nutrimage



def product_view(request,productid):
    product = Product.objects.get(pk=productid)
    nutriscore = product.nutriScore

    nutriscore_image = Nutrimage.objects.get(name=nutriscore)
    
    context = {"product": product, "nutri_img":nutriscore_image}
    
    return render(request, 'product.html', context)

def search_results(request):
    q = request.GET.get('q',None)
    if q:
        products = Product.objects.filter(Q(name__icontains=q)).order_by('name')[:10]
    else:
        return redirect('mainpage')
    nutriscore_image = Nutrimage.objects.all()
    
    context = {'products':products, 'nutrimage':nutriscore_image}
    return render(request, 'research_result.html', context)

def substitution_results(request,productid):
    base_product = Product.objects.get(pk=productid)
    base_product_categories = base_product.category.all()
    base_nutri = base_product.nutriScore
    substitutes_list = []
    subtitutes = Product.objects.filter(category__in=base_product_categories)
    for sub in subtitutes:
        if sub.nutriScore == "a":
            substitutes_list.append(sub)
        elif sub.nutriScore < base_nutri:
            substitutes_list.append(sub)
    if len(substitutes_list) > 0:
        ten_substitutes = substitutes_list[:11]
    else:
        ten_substitutes = None

    context = {'productid':productid, 'baseproduct':base_product, 'substitutes':ten_substitutes}
    return render(request, 'result.html', context)

