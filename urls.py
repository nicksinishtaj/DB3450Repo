from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.views import LoginView
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', LoginView.as_view(template_name='DB3450Repo/userLogin.html'), name="Login"),
    path('inventory/', views.inventory_view, name='inventory'),
    path('inventoryQuery', views.inventoryQuery_view, name='inventoryQuery'),
    path('inventoryDetails', views.inventoryDetails_view, name='inventoryDetails'),
    path('employeePermission/', views.employeePermission_view, name='employee_permission'),
    path('employeePermissionAdd', views.employeePermissionAdd_view, name='employeePermissionAdd'),
    path('employeePermissionAfterAdd', views.employeePermissionAfterAdd_view, name='employeePermissionAfterAdd'),
    path('employeePermissionQuery', views.employeePermissionQuery_view, name='employeePermissionQuery'),
    path('employeePermissionDetails', views.employeePermissionDetails_view, name='employeePermissionDetails'),
]
