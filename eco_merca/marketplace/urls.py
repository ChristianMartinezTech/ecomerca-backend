from django.urls import path
from . import views

app_name = "marketplace"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:brand_id>/", views.brand_detail, name="brand_detail"),
    path("brand/<int:brand_id>/", views.brand_detail, name="brand_detail"),
    path("product/<int:product_id>/", views.product_detail, name="product_detail"),
]