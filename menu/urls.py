from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('table/',table,name='table'),
    path('menu/',menu,name='menu'),
    path('customer/<str:pk>',customer,name='customer'),
    path('customert/<str:tableno>',customer2,name='customer2'),
    path('order/<str:custid>',order,name='order'),
    path('kitchen/',kitchen,name='kitchen'),
]
