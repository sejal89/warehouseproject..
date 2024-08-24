from django.contrib import admin
from django.urls import path
from .views import Loginviews, Addproduct, helloView, editproduct, editProductView, delete, order, OrderView

urlpatterns  = [
    path("login/",Loginviews),
    path("Addproduct/",Addproduct, name='Addproduct'),
    path("helloView/",helloView, name='helloView'),
    path("edit-product/",editProductView, name='edit-product'),
    path("edit-product/edit/",editproduct),
    path('delete/<int:id>', delete),
    path('order', order, name='order'),
    path('orderview', OrderView, name='orderview'),
]
