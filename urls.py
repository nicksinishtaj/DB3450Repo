from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.views import LoginView
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    # Login page
    path('login/', LoginView.as_view(template_name='DB3450Repo/userLogin.html'), name="Login"),
    # List the inventory
    path('inventory/', views.inventory_view, name='inventory'),
    # Search the inventory
    path('inventoryQuery', views.inventoryQuery_view, name='inventoryQuery'),
    # Get inventory details; comes after inventoryQuery
    path('inventoryDetails', views.inventoryDetails_view, name='inventoryDetails'),
    # Add items to the database inventory
    path('inventoryAdd', views.inventoryAdd_view, name='inventoryAdd'),
    # Get inventory details; comes after inventoryAdd
    path('inventoryAfterAdd', views.inventoryAfterAdd_view,
         name='inventoryAfterAdd'),
    # Update item information in the database inventory
    path('inventoryUpdate', views.inventoryUpdate_view, name='inventoryUpdate'),
    # Get inventory details; comes after inventoryUpdate
    path('inventoryAfterUpdate', views.inventoryAfterUpdate_view,
         name='inventoryAfterUpdate'),
    # List employee permissions
    path('employeePermission/', views.employeePermission_view,
         name='employee_permission'),
    # Add employee permissions
    path('employeePermissionAdd', views.employeePermissionAdd_view,
         name='employeePermissionAdd'),
    # Get employee permissions; comes after employeePermissionAdd
    path('employeePermissionAfterAdd', views.employeePermissionAfterAdd_view,
         name='employeePermissionAfterAdd'),
    # Search employee permission levels
    path('employeePermissionQuery', views.employeePermissionQuery_view,
         name='employeePermissionQuery'),
    # Get employee permission information; comes after employeePermissionQuery
    path('employeePermissionDetails', views.employeePermissionDetails_view,
         name='employeePermissionDetails'),
    # Remove employee permissions
    path('employeePermissionDelete', views.employeePermissionDelete_view,
         name='employeePermissionDelete'),
    # Get employee permission informaion; comes after employeePermissionDelete
    path('employeePermissionAfterDelete', views.employeePermissionAfterDelete_view,
         name='employeePermissionAfterDelete'),
    # Add or Update a supplier's inventory record
    path('inventorySupplierAddOrUpdate',
         views.inventorySupplierAdd_view, name='inventorySupplierAdd'),
    # Get a supplier's inventory record; comes after inventorySupplierAddOrUpdate
    path('inventorySupplierAfterAddOrUpdate',
         views.inventorySupplierAfterAdd_view, name='inventorySupplierAfterAdd'),
    # Remove supplier inventory records
    path('inventorySupplierDelete', views.inventorySupplierDelete_view,
         name='inventorySupplierDelete'),
    # Get supplier inventory records; comes after inventorySupplierDelete
    path('inventorySupplierAfterDelete', views.inventorySupplierAfterDelete_view,
         name='inventorySupplierAfterDelete'),
    # Add or update supplier information
    path('supplierAddOrUpdate', views.supplierAddOrUpdate_view,
         name='supplierAddOrUpdate'),
    # Get supplier information; comes after supplierAddOrUpdate
    path('supplierAfterAddOrUpdate', views.supplierAfterAddOrUpdate_view,
         name='supplierAfterAddOrUpdate'),
    # Get project name and status
    path('projectBaseInfo', views.projectBaseInfo_view, name='projectBaseInfo'),
    # Get project budget and expenditures
    path('projectBudget', views.projectBudget_view, name='projectBudget'),
    # Get project employees
    path('projectEmployees', views.projectEmployees_view, name='projectEmployees'),
    # Get project inventory
    path('projectInventory', views.projectInventory_view, name='projectInventory'),
    # Search employee hours
    path('employeeHoursQuery', views.employeeHoursQuery_view,
         name='employeeHoursQuery'),
    # Get employee hours information; comes after employeeHoursQuery
    path('employeeHoursDetails', views.employeeHoursDetails_view,
         name='employeeHoursDetails'),
    # Add Employee Hours
    path('employeeHoursAdd', views.employeeHoursAdd_view, name='employeeHoursAdd'),
]
