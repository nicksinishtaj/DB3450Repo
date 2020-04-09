from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.views import LoginView
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', LoginView.as_view(template_name='construction_company/userLogin.html'), name="Login"),
    path('inventory/', views.inventory_view, name='inventory'),
    path('inventoryQuery', views.inventoryQuery_view, name='inventoryQuery'),
    path('inventoryDetails', views.inventoryDetails_view, name='inventoryDetails'),

]
