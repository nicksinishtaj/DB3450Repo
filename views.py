from django.shortcuts import render
from django.http import HttpResponse
from construction_company.models import Inventory
from construction_company.models import InventorySupplier
from construction_company.models import EmployeePermission
from construction_company.models import Employee
from construction_company.models import Permission
from construction_company.models import Project
from construction_company.models import SupplierCompany
from datetime import date
from django.db import connection
    

def index(request):
    return render(request, 'construction_company/home.html')

def inventory_view(request):
    query_set = Inventory.objects.raw('SELECT * FROM inventory')
    context = {
        'object_instance' : query_set
    }
    return render(request, 'construction_company/inventory.html', context)

def employeePermission_view(request):
    query_set = EmployeePermission.objects.raw('SELECT * FROM employee_permission')
    employee_query_set = Employee.objects.raw('SELECT * FROM employee')
    permission_query_set = Permission.objects.raw('SELECT * FROM permission')
    employee_query_set_append = []
    permission_query_set_append = []

    for employeePermission in query_set:
                employee_query_set_append.append(employeePermission.employee)
                permission_query_set_append.append(employeePermission.permission_level)

    context = {
        'employee_object_instance' : employee_query_set_append,
        'permission_object_instance' : permission_query_set_append
    }
    return render(request, 'construction_company/employeePermission.html', context)

def employeePermissionQuery_view(request):
    return render(request, 'construction_company/employeePermissionQuery.html')

def employeePermissionDetails_view(request):
    employee_id_request = request.GET['employee_id']

    query_set = EmployeePermission.objects.raw('SELECT * FROM employee_permission')
    employee_query_set = Employee.objects.raw('SELECT * FROM employee')
    permission_query_set = Permission.objects.raw('SELECT * FROM permission')

    employee_query_set_append = []
    permission_query_set_append = []

    validEmployee = Employee.objects.get(employee_id = employee_id_request)

    for employeePermission in query_set:
                if(employeePermission.employee == validEmployee):
                    employee_query_set_append.append(employeePermission.employee)
                    permission_query_set_append.append(employeePermission.permission_level)
    

    context = {
        'employee_object_instance' : employee_query_set_append,
        'permission_object_instance' : permission_query_set_append
    }
    return render(request, 'construction_company/employeePermissionDetails.html', context)


def employeePermissionAdd_view(request):
    query_set = EmployeePermission.objects.raw('SELECT * FROM employee_permission')
    employee_query_set = Employee.objects.raw('SELECT * FROM employee')
    permission_query_set = Permission.objects.raw('SELECT * FROM permission')
    employee_query_set_append = []
    permission_query_set_append = []

    for employeePermission in query_set:
                employee_query_set_append.append(employeePermission.employee)
                permission_query_set_append.append(employeePermission.permission_level)

    context = {
        'employee_object_instance' : employee_query_set_append,
        'permission_object_instance' : permission_query_set_append
    }
    return render(request, 'construction_company/employeePermissionAdd.html', context)

def employeePermissionAfterAdd_view(request):
    employee_id = request.GET['employee_id']
    permission_level = request.GET['permission_level']
    project_id = request.GET['project_id']
    employee_permission_start = date.today()

    validEmployee = Employee.objects.get(employee_id = employee_id)
    validPermission = Permission.objects.get(permission_level = permission_level)
    validProject = Project.objects.get(project_id = project_id)

    query_set_append = []
    query_set = EmployeePermission.objects.raw('SELECT * FROM employee_permission')
    new_query_set = query_set
    employee_query_set = Employee.objects.raw('SELECT * FROM employee')
    permission_query_set = Permission.objects.raw('SELECT * FROM permission')
    project_query_set = Project.objects.raw('SELECT * FROM project')
    employee_query_set_append = []
    permission_query_set_append = []

    x = 0
    
    for object in query_set:
        query_set_append.append(object)
        if(validEmployee == object.employee and validPermission == object.permission_level and validProject == object.project):
            x += 1

    if(x == 0):
        newEmployeePermission = EmployeePermission(employee_id = validEmployee.employee_id, permission_level = validPermission, project_id = project_id, employee_permission_start = employee_permission_start )
        newEmployeePermission.save()
        new_query_set = EmployeePermission.objects.raw('SELECT * FROM employee_permission')
        # EmployeePermission.INSERT('INSERT INTO employee_permission (employee_id, permission_level, project_id, employee_permission_start)' 'VALUES (%s, %s, %s, %s),' [employee_id, permission_level, project_id, employee_permission_start])
        # new_query_set = EmployeePermission.objects.raw('SELECT * FROM employee_permission')

    employee_query_set_final = Employee.objects.raw('SELECT * FROM employee')
    permission_query_set_final = Permission.objects.raw('SELECT * FROM permission')

    for employeePermission in new_query_set:
                employee_query_set_append.append(employeePermission.employee)
                permission_query_set_append.append(employeePermission.permission_level)

    context = {
        'employee_object_instance' : employee_query_set_append,
        'permission_object_instance' : permission_query_set_append
    }
    return render(request, 'construction_company/employeePermission.html', context)


def employeePermissionDelete_view(request):
    query_set = EmployeePermission.objects.raw('SELECT * FROM employee_permission')
    employee_query_set = Employee.objects.raw('SELECT * FROM employee')
    permission_query_set = Permission.objects.raw('SELECT * FROM permission')
    employee_query_set_append = []
    permission_query_set_append = []

    for employeePermission in query_set:
                employee_query_set_append.append(employeePermission.employee)
                permission_query_set_append.append(employeePermission.permission_level)

    context = {
        'employee_object_instance' : employee_query_set_append,
        'permission_object_instance' : permission_query_set_append
    }
    return render(request, 'construction_company/employeePermissionDelete.html', context)

def employeePermissionAfterDelete_view(request):
    employee_id = request.GET['employee_id']
    permission_level = request.GET['permission_level']
    project_id = request.GET['project_id']
    employee_permission_start = date.today()

    validEmployee = Employee.objects.get(employee_id = employee_id)
    validPermission = Permission.objects.get(permission_level = permission_level)
    validProject = Project.objects.get(project_id = project_id)

    query_set = EmployeePermission.objects.raw('SELECT * FROM employee_permission')
    
    for employeePermission in query_set:
        if(employeePermission.employee == validEmployee and employeePermission.permission_level == validPermission and employeePermission.project == validProject):
            employeePermission.delete()

    new_query_set = EmployeePermission.objects.raw('SELECT * FROM employee_permission')
    employee_query_set_final = Employee.objects.raw('SELECT * FROM employee')
    permission_query_set_final = Permission.objects.raw('SELECT * FROM permission')
    employee_query_set_append = []
    permission_query_set_append = []

    for employeePermission in new_query_set:
                employee_query_set_append.append(employeePermission.employee)
                permission_query_set_append.append(employeePermission.permission_level)

    context = {
        'employee_object_instance' : employee_query_set_append,
        'permission_object_instance' : permission_query_set_append
    }
    return render(request, 'construction_company/employeePermissionAfterDelete.html', context)



    
def inventoryQuery_view(request):
    return render(request, 'construction_company/inventoryQuery.html')

def inventoryDetails_view(request):
    inventory_name = request.GET['inventory_name']
    inventory_description = request.GET['inventory_description']
    query_set_append = []
    query_set = Inventory.objects.raw('SELECT * FROM inventory')
    for object in query_set:
            if(inventory_name == object.inventory_name):
                query_set_append.append(object)


    context = {
        'object_instance' : query_set_append
    }

    return render(request, 'construction_company/inventoryDetails.html', context)

def inventoryAdd_view(request):
    query_set = Inventory.objects.raw('SELECT * FROM inventory')

    context = {
        'object_instance': query_set
    }
    return render(request, 'construction_company/inventoryAdd.html', context)

def inventoryAfterAdd_view(request):
    inventory_name_request = request.GET['inventory_name']
    inventory_description_request = request.GET['inventory_description']
    newInventory = Inventory(inventory_name = inventory_name_request, inventory_description = inventory_description_request)
    newInventory.save()
    query_set_append = []
    query_set = Inventory.objects.raw('SELECT * FROM inventory')

    context = {
        'object_instance' : query_set
    }

    return render(request, 'construction_company/inventoryAfterAdd.html', context)

def inventoryUpdate_view(request):
    query_set = Inventory.objects.raw('SELECT * FROM inventory')

    context = {
        'object_instance': query_set
    }
    return render(request, 'construction_company/inventoryUpdate.html', context)

def inventoryAfterUpdate_view(request):
    inventory_id_request = request.GET['inventory_id']
    inventory_name_request = request.GET['inventory_name']
    inventory_description_request = request.GET['inventory_description']
    # newInventory = Inventory(inventory_name = inventory_name_request, inventory_description = inventory_description_request)

    # query_set_append = []

    newInventory = Inventory.objects.get(inventory_id = inventory_id_request)
    newInventory.inventory_name = inventory_name_request
    newInventory.inventory_description = inventory_description_request
    newInventory.save()

    query_set = Inventory.objects.raw('SELECT * FROM inventory')


    context = {
        'object_instance' : query_set
    }

    return render(request, 'construction_company/inventoryAfterUpdate.html', context)

def inventorySupplierAdd_view(request):
    query_set = InventorySupplier.objects.raw('SELECT * FROM inventory_supplier')
    inventory_query_set = Inventory.objects.raw('SELECT * FROM inventory')
    supplier_query_set = SupplierCompany.objects.raw('SELECT * FROM supplier_company')
    inventory_query_set_append = []
    supplier_query_set_append = []

    for inventorySupplier in query_set:
        inventory_query_set_append.append(inventorySupplier.inventory_supplier_inventory)
        supplier_query_set_append.append(inventorySupplier.supplier)



    context = {
        'object_instance': query_set,
        'inventory_object_instance': inventory_query_set_append,
        'supplier_object_instance': supplier_query_set_append
    }
    return render(request, 'construction_company/inventorySupplierAddOrUpdate.html', context)

def inventorySupplierAfterAdd_view(request):
    inventory_name_request = request.GET['inventory_name']
    supplier_company_request = request.GET['supplier_company']
    inventory_supplier_cost_request = request.GET['inventory_supplier_cost']
    inventory_supplier_amount_request = request.GET['inventory_supplier_amount']
    inventory_supplier_notes_request = request.GET['inventory_supplier_notes']
    inventory_supplier_preferred_request = request.GET['inventory_supplier_preferred']

    inventory_supplier_cost_int = int(inventory_supplier_cost_request)
    inventory_supplier_amount_int = int(inventory_supplier_amount_request)
    inventory_supplier_preferred_int = int(inventory_supplier_preferred_request)


    final_query_set = []
    inventory_query_set_append = []
    supplier_query_set_append = []

    inventory_query_set = Inventory.objects.raw('SELECT * FROM inventory')
    supplier_query_set = SupplierCompany.objects.raw('SELECT * FROM supplier_company')

    newInventory = Inventory.objects.get(inventory_name = inventory_name_request)
    newSupplier = SupplierCompany.objects.get(supplier_company_name = supplier_company_request)

    validateInventory = InventorySupplier.objects.get(inventory_supplier_inventory = newInventory, supplier = newSupplier)

    if(validateInventory is not None):
        cursor = connection.cursor()
        cursor.execute('UPDATE inventory_supplier SET inventory_supplier_cost = %s, inventory_supplier_amount = %s, inventory_supplier_notes = %s, inventory_supplier_preferred = %s WHERE INVENTORY_SUPPLIER_INVENTORY_ID = %s AND SUPPLIER_ID = %s', [inventory_supplier_cost_int, inventory_supplier_amount_int, inventory_supplier_notes_request, inventory_supplier_preferred_int, validateInventory.inventory_supplier_inventory.inventory_id, validateInventory.supplier.supplier_company_id])

    if((newInventory is not None or newSupplier is not None) and validateInventory is None):
        newInventorySupplier = InventorySupplier(inventory_supplier_inventory = newInventory, supplier = newSupplier, inventory_supplier_cost = inventory_supplier_cost_request, inventory_supplier_amount = inventory_supplier_amount_request, inventory_supplier_notes = inventory_supplier_notes_request, inventory_supplier_preferred = inventory_supplier_preferred_request )
        cursor = connection.cursor()
        cursor.execute('INSERT INTO inventory_supplier VALUES (%s,%s,%s,%s,%s,%s)', [newInventory.inventory_id, newSupplier.supplier_company_id, inventory_supplier_cost_int, inventory_supplier_amount_int, inventory_supplier_notes_request, inventory_supplier_preferred_int])
        connection.commit()

    query_set = InventorySupplier.objects.raw('SELECT * FROM inventory_supplier')

    for inventorySupplier in query_set:
        inventory_query_set_append.append(inventorySupplier.inventory_supplier_inventory)
        supplier_query_set_append.append(inventorySupplier.supplier)

    context = {
        'object_instance': query_set,
        'inventory_object_instance': inventory_query_set_append,
        'supplier_object_instance': supplier_query_set_append
    }

    return render(request, 'construction_company/inventorySupplierAfterAddOrUpdate.html', context)


def inventorySupplierDelete_view(request):
    query_set = InventorySupplier.objects.raw('SELECT * FROM inventory_supplier')
    inventory_query_set = Inventory.objects.raw('SELECT * FROM inventory')
    supplier_query_set = SupplierCompany.objects.raw('SELECT * FROM supplier_company')
    inventory_query_set_append = []
    supplier_query_set_append = []

    for inventorySupplier in query_set:
        inventory_query_set_append.append(inventorySupplier.inventory_supplier_inventory)
        supplier_query_set_append.append(inventorySupplier.supplier)



    context = {
        'object_instance': query_set,
        'inventory_object_instance': inventory_query_set_append,
        'supplier_object_instance': supplier_query_set_append
    }
    return render(request, 'construction_company/inventorySupplierDelete.html', context)

def inventorySupplierAfterDelete_view(request):
    inventory_name_request = request.GET['inventory_name']
    supplier_company_request = request.GET['supplier_company']
    final_query_set = []
    inventory_query_set_append = []
    supplier_query_set_append = []

    inventory_query_set = Inventory.objects.raw('SELECT * FROM inventory')
    supplier_query_set = SupplierCompany.objects.raw('SELECT * FROM supplier_company')

    newInventory = Inventory.objects.get(inventory_name = inventory_name_request)
    newSupplier = SupplierCompany.objects.get(supplier_company_name = supplier_company_request)

    validateInventory = InventorySupplier.objects.get(inventory_supplier_inventory = newInventory, supplier = newSupplier)
    cursor = connection.cursor()
    cursor.execute('DELETE FROM inventory_supplier WHERE INVENTORY_SUPPLIER_INVENTORY_ID = %s AND SUPPLIER_ID = %s', [newInventory.inventory_id, newSupplier.supplier_company_id])
    connection.commit()

    query_set = InventorySupplier.objects.raw('SELECT * FROM inventory_supplier')

    for inventorySupplier in query_set:
        inventory_query_set_append.append(inventorySupplier.inventory_supplier_inventory)
        supplier_query_set_append.append(inventorySupplier.supplier)

    context = {
        'object_instance': query_set,
        'inventory_object_instance': inventory_query_set_append,
        'supplier_object_instance': supplier_query_set_append
    }

    return render(request, 'construction_company/inventorySupplierAfterDelete.html', context)

def supplierAddOrUpdate_view(request):
    query_set = SupplierCompany.objects.raw('SELECT * FROM supplier_company')

    context = {
        'object_instance': query_set,
    }
    return render(request, 'construction_company/supplierAddOrUpdate.html', context)

def supplierAfterAddOrUpdate_view(request):
    id_req = request.GET['supplier_company_id']
    name_req = request.GET['supplier_company_name']
    streetOne_req = request.GET['supplier_company_streetOne']
    streetTwo_req = request.GET['supplier_company_streetTwo']
    city_req = request.GET['supplier_company_city']
    state_req = request.GET['supplier_company_state']
    zip_req = request.GET['supplier_company_zip']
    notes_req = request.GET['supplier_company_notes']
    id_req_int = 0
    validateSupplier = None

    if(id_req is not None and id_req != ''):
        id_req_int = int(id_req)
        validateSupplier = SupplierCompany.objects.get(supplier_company_id = id_req_int)
    else:
        validateSupplier = None

    if(validateSupplier is not None):
        cursor = connection.cursor()
        cursor.execute('UPDATE supplier_company SET supplier_company_name = %s, supplier_company_street1 = %s, supplier_company_street2 = %s, supplier_company_city = %s, supplier_company_state = %s, supplier_company_zip = %s, supplier_company_notes = %s WHERE SUPPLIER_COMPANY_ID = %s', [name_req, streetOne_req, streetTwo_req, city_req, state_req, zip_req, notes_req, id_req_int])
        connection.commit()
    
    if(validateSupplier is None):
        cursor = connection.cursor()
        cursor.execute('INSERT INTO supplier_company (supplier_company_name, supplier_company_street1, supplier_company_street2, supplier_company_city, supplier_company_state, supplier_company_zip, supplier_company_notes) VALUES (%s,%s,%s,%s,%s,%s,%s)', [name_req, streetOne_req, streetTwo_req, city_req, state_req, zip_req, notes_req])
        connection.commit()

    query_set = SupplierCompany.objects.raw('SELECT * FROM supplier_company')

    context = {
        'object_instance': query_set,
    }
    return render(request, 'construction_company/supplierAfterAddOrUpdate.html', context)
        
