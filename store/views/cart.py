from django.shortcuts import render , redirect

from django.shortcuts import render, redirect,\
    HttpResponseRedirect
from django.views import View
from store.models.Product import Product

class Cart(View):
    def get(self , request):
        ids=list(request.session.get('cart').keys())
        products=Product.get_products_by_id(ids)
        print(products)
        return render(request , 'cart.html',{'products':products} )

