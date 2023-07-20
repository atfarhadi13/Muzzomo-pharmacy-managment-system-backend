from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('customer_view' , customer_view , name="customer_view"),
    path('add_customer_view' , add_customer_view , name="add_customer_view"),
]