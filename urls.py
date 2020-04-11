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
    path('inventoryAdd', views.inventoryAdd_view, name='inventoryAdd'),
    path('inventoryAfterAdd', views.inventoryAfterAdd_view, name='inventoryAfterAdd'),
    path('inventoryUpdate', views.inventoryUpdate_view, name='inventoryUpdate'),
    path('inventoryAfterUpdate', views.inventoryAfterUpdate_view, name='inventoryAfterUpdate'),
    path('employeePermission/', views.employeePermission_view, name='employee_permission'),
    path('employeePermissionAdd', views.employeePermissionAdd_view, name='employeePermissionAdd'),
    path('employeePermissionAfterAdd', views.employeePermissionAfterAdd_view, name='employeePermissionAfterAdd'),
    path('employeePermissionQuery', views.employeePermissionQuery_view, name='employeePermissionQuery'),
    path('employeePermissionDetails', views.employeePermissionDetails_view, name='employeePermissionDetails'),
    path('employeePermissionDelete', views.employeePermissionDelete_view, name='employeePermissionDelete'),
    path('employeePermissionAfterDelete', views.employeePermissionAfterDelete_view, name='employeePermissionAfterDelete'),
    path('inventorySupplierAddOrUpdate', views.inventorySupplierAdd_view, name='inventorySupplierAdd'),
    path('inventorySupplierAfterAddOrUpdate', views.inventorySupplierAfterAdd_view, name='inventorySupplierAfterAdd'),
    path('inventorySupplierDelete', views.inventorySupplierDelete_view, name='inventorySupplierDelete'),
    path('inventorySupplierAfterDelete', views.inventorySupplierAfterDelete_view, name='inventorySupplierAfterDelete'),
    path('supplierAddOrUpdate', views.supplierAddOrUpdate_view, name='supplierAddOrUpdate'),
    path('supplierAfterAddOrUpdate', views.supplierAfterAddOrUpdate_view, name='supplierAfterAddOrUpdate')
]
