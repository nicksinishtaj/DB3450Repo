from django.contrib import admin
from construction_company.models import CustomerCompany
from construction_company.models import CustomerContact
from construction_company.models import Employee
from construction_company.models import EmployeeHours
from construction_company.models import EmployeePermission
from construction_company.models import Inventory
from construction_company.models import InventorySupplier
from construction_company.models import Permission
from construction_company.models import Project
from construction_company.models import ProjectInventory
from construction_company.models import Purchase
from construction_company.models import SupplierCompany
from construction_company.models import SupplierContact

# Register your models here.

admin.site.register(CustomerCompany)
admin.site.register(CustomerContact)
admin.site.register(Employee)
admin.site.register(EmployeeHours)
admin.site.register(EmployeePermission)
admin.site.register(Inventory)
admin.site.register(InventorySupplier)
admin.site.register(Permission)
admin.site.register(Project)
admin.site.register(ProjectInventory)
admin.site.register(Purchase)
admin.site.register(SupplierCompany)
admin.site.register(SupplierContact)

