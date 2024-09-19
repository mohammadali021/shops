from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from carts.cart import Cart
from shops.models import Product


def ViewCarts(request):
    cart = Cart(request)
    cart_pro = cart.get_prods()
    # quantities = cart.get_quants()
    return render(request, 'carts/index.html' , {"cart_pro":cart_pro})


def CartAdd(request):
    cart = Cart(request)
    if request.POST.get('action')=='post':
        product_id = int(request.POST.get('product_id'))
        # product_qyt = int(request.POST.get('product_qyt'))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product)
        cart_count = cart.__len__()
        # response = JsonResponse({'product name':product.name})
        response = JsonResponse({'cart_count':cart_count})

        return response


# Create your views here.
