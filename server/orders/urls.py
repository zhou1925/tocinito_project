from django.urls import path
from . import views
                                                 
                                                                       
urlpatterns = [
    path("", views.get_orders, name="orders"),
    path("products/", views.get_products),
    path("create/", views.create_order),
    path("popular/", views.get_popular_products, name="popular")
]
