from django.contrib import admin
from DB3450Repo.models import CustomerCompany
from DB3450Repo.models import CustomerContact
from DB3450Repo.models import Employee
from DB3450Repo.models import EmployeeHours
from DB3450Repo.models import EmployeePermission
from DB3450Repo.models import Inventory
from DB3450Repo.models import InventorySupplier
from DB3450Repo.models import Permission
from DB3450Repo.models import Project
from DB3450Repo.models import ProjectInventory
from DB3450Repo.models import Purchase
from DB3450Repo.models import SupplierCompany
from DB3450Repo.models import SupplierContact

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

