from django.shortcuts import render
from django.db.models import Q
from products.models import Product,Category


def mainpage(request):
    context = {}
        
    return render(request, 'mainpage.html',context)
    
    
def legalpage(request):
    
    return render(request, 'legals.html', {})