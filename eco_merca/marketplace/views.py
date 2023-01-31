from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Brand, Product


def index(request):
    latest_brand_list = Brand.objects.all()
    return render(request, "marketplace/index.html", {
        "latest_brand_list": latest_brand_list
    })


def brand_detail(request, brand_id):
    """ Brand details """
    brand = get_object_or_404(Brand, pk=brand_id)
    render(request, "marketplace/detail.html", {
        "brand":brand
    })


def product_detail(request, brand_id):    
    """ Product details """
    pass


def brand_products(request, brand_id):
    """ Get all products associated with a brand """
    pass


def buy_product(reques, brand_id):
    """ Form to buy a product """
    return HttpResponse(f"¿Cual producto quieres comprar?", {brand_id})
