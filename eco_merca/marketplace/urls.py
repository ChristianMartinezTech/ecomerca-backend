from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("brand/<int:brand_id>/", views.brand_detail, name="index"),
    path("<int:brand_id>/", views.brand_detail, name="index"),
    path("product/<int:product_id>/", views.product_detail, name="index"),
]