from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop, name='shop'),
    path('basket/', views.basket, name='basket'),
    path('checkout/', views.checkout, name='checkout'),
    path('imprint/', views.imprint, name='imprint')
]