from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Brand


# Views
def index(request):
    latest_brand_list = Brand.objects.all()
    return render(request, "marketplace/index.html", {
        "latest_brand_list": latest_brand_list
    })

def brand_detail(request, brand_id):
    brand = get_object_or_404(Brand, pk=brand_id)
    return render(request, "marketplace/brand_detail.html", {
        "brand": brand
    })

def product_detail(request, product_id):
    return HttpResponse(f"Estas viendo el producto {product_id}")
