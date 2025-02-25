from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    # Home page
    path('', views.home, name='home'),
    # Login page
    path('login/', LoginView.as_view(template_name='DB3450Repo/userLogin.html'), name="Login"),
    path('homeII', views.homeII_view, name='homeII'),

    # INVENTORY PATH INFORMATION
    # List the inventory
    path('inventoryBaseInfo/', views.inventoryBaseInfo_view,
         name='inventoryBaseInfo'),
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
    # Get inventory purchase information
    path('inventoryPurchaseInfo', views.inventoryPurchaseInfo_view,
         name='inventoryPurchaseInfo'),
    # Add or Update a supplier's inventory record
    path('inventorySupplierView', views.inventorySupplierView_view,
         name='inventorySupplierView'),
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


    # EMPLOYEE PATH INFORMATION
    # Get employee landing page; comes after clicking on 'Employee' button on the home page
    path('employeeLanding', views.employeeLanding_view, name='employeeLanding'),
    # Get employee purchase info
    path('employeePurchaseInfo', views.employeePurchaseInfo_view,
         name='employeePurchaseInfo'),
    # Get employee permissions
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
    # Search employee hours
    path('employeeHoursQuery', views.employeeHoursQuery_view,
         name='employeeHoursQuery'),
    # Get employee hours information; comes after employeeHoursQuery
    path('employeeHoursDetails', views.employeeHoursDetails_view,
         name='employeeHoursDetails'),
    # Add Employee Hours
    path('employeeHoursAdd', views.employeeHoursAdd_view, name='employeeHoursAdd'),
    # Get employee hours information; comes after employeeHoursQuery
    path('employeeHoursEdit', views.employeeHoursEdit_view,
         name='employeeHoursEdit'),
    # Search employees to update hours
    path('employeeHoursEditSelect', views.employeeHoursEditSelect_view,
         name='employeeHoursEditSelect'),


    # SUPPLIER PATH INFORMATION
    # Get supplier landing page; comes after clicking on 'Supplier' button on the home page
    path('supplierLanding', views.supplierLanding_view, name='supplierLanding'),
    # Add or update supplier information
    path('supplierView', views.supplierView_view, name='supplierView'),
    path('supplierAddOrUpdate', views.supplierAddOrUpdate_view,
         name='supplierAddOrUpdate'),
    # Get supplier information; comes after supplierAddOrUpdate
    path('supplierAfterAddOrUpdate', views.supplierAfterAddOrUpdate_view,
         name='supplierAfterAddOrUpdate'),
    # Updated Supllier Contact
    path('supplierContactUpdate', views.supplierContactUpdate_view,
         name=' supplierContactUpdate'),
    # Gets updated supplier Contact; comes after supplierContactUpdate
    path('supplierContactAfterUpdate', views.supplierContactAfterUpdate_view,
         name='supplierContactAfterUpdate'),
    # Gets the Supplier that needs to be deleted
    path('supplierCompanyDelete', views.supplierCompanyDelete_view,
         name=' supplierCompanyDelete'),


    # PROJECT PATH INFORMATION
    # Get project name and status; comes after clicking on 'Project' button on home page
    path('projectBaseInfo', views.projectBaseInfo_view, name='projectBaseInfo'),
    # Add a new project
    path('projectAdd', views.projectadd_view, name='project_add'),
    # Get project budget and expenditures
    path('projectBudget', views.projectBudget_view, name='projectBudget'),
    # Get project employees
    path('projectEmployees', views.projectEmployees_view, name='projectEmployees'),
    # Get project inventory
    path('projectInventory', views.projectInventory_view, name='projectInventory'),
    # Get project purchase information
    path('projectPurchases', views.projectPurchases_view, name='projectPurchases'),
    # Add Supplier Contact
    path('supplierContactAdd', views.supplierContactAdd_view,
         name=' supplierContactAdd'),
    # Gets added supplier Contact; comes after supplierContactAdd
    path('supplierContactAfterAdd', views.supplierContactAfterAdd_view,
         name='supplierContactAfterAdd'),
    # Updated Supllier Contact
    path('supplierContactUpdate', views.supplierContactUpdate_view,
         name=' supplierContactUpdate'),
    # Gets updated supplier Contact; comes after supplierContactUpdate
    path('supplierContactAfterUpdate', views.supplierContactAfterUpdate_view,
         name='supplierContactAfterUpdate'),
    # Gets Supplier Contact ID; and sets the supplier_contact_current value to 0
    path('supplierContactDelete', views.supplierContactDelete_views,
         name='supplierContactDelete'),
    # Get project purchase information
    path('projectPurchases', views.projectPurchases_view, name='projectPurchases'),


    # CUSTOMER PATH INFORMATION
    # Gets customer landing page; comes after clicking 'customer' on main page
    path('customerLanding', views.customerLanding_view, name='customerLanding'),
    # Gets information for new customer contact and puts it into the system
    path('customerContactAdd', views.customerContactAdd_view,
         name='customerContactAdd'),
    # Get a list of employees managed by a given employee
    path('employeeEmployeesManaged', views.employeeEmployeesManaged_view,
         name='employeeEmployeesManaged'),
    # Get a list of customers managed by a given employee
    path('employeeCustomersManaged', views.employeeCustomersManaged_view,
         name='employeeCustomersManaged'),
    # Add new employees
    path('employeeAdd', views.employeeAdd_view,
         name='employeeAdd'),
    # Select Employee to Update
    path('employeeUpdateSelect', views.employeeUpdateSelect_view,
         name='employeeUpdateSelect'),
    # Update employees
    path('employeeUpdate', views.employeeUpdate_view,
         name='employeeUpdate'),
    # Remove employees
    path('employeeDelete', views.employeeDelete_view,
         name='employeeDelete'),
    # Employee home
    path('employeeHome', views.employeeHome_view,
         name='employeeHome'),
    path('customerContactAdd', views.customerContactAdd_view,
         name='customerContactAdd'),
    # Gets the information needed for the customer contact
    path('customerContactUpdate', views.customerContactUpdate_view,
         name='customerContactUpdate'),
    # Gets the information requried to update values in the Customer_company table
    path('customerCompanyUpdate', views.customerCompanyUpdate_view,
         name='customerCompanyUpdate'),
    # Gets the information for adding a new Customer into the system
    path('customerCompanyAdd', views.customerCompanyAdd_view,
         name='customerCompanyAdd'),
    # Employee Hours home
    path('employeeHoursHome', views.employeeHoursHome_view,
         name='employeeHoursHome'),
    # Employee Permission home
    path('employeePermissionsHome', views.employeePermissionsHome_view,
         name='employeePermissionsHome'),
]
