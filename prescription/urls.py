from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('order_view' , order_view , name="order_view"),
    path('add_order_view' , add_order_view , name="add_order_view"),
]