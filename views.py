from datetime import date, datetime
from decimal import Decimal

import django
from django.db import connection
from django.http import HttpResponse
from django.shortcuts import render

from DB3450Repo.models import (CustomerCompany, Employee, EmployeeHours,
                               EmployeePermission, Inventory,
                               InventorySupplier, Permission, Project,
                               ProjectInventory, SupplierCompany,
                               SupplierContact)

# GENERAL LINK HANDLING
def home(request):
    return render(request, 'DB3450Repo/home.html')

def homeII_view(request):
    return render(request, 'DB3450Repo/homeII.html')

# INVENTORY LINK HANDLING

def inventory_view(request):
    query_set = Inventory.objects.raw('SELECT * FROM inventory')
    context = {
        'object_instance': query_set
    }
    return render(request, 'DB3450Repo/inventory.html', context)


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
    return render(request, 'DB3450Repo/employeePermission.html', context)

def employeePermissionQuery_view(request):
    return render(request, 'DB3450Repo/employeePermissionQuery.html')

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

    return render(request, 'DB3450Repo/employeePermissionDetails.html', context)


def employeePermissionAdd_view(request):
    query_set = EmployeePermission.objects.raw('SELECT * FROM employee_permission')
    employee_query_set = Employee.objects.raw('SELECT * FROM employee')
    permission_query_set = Permission.objects.raw('SELECT * FROM permission')
    project_query_set = Project.objects.raw('SELECT * FROM project')
    employee_query_set_append = []
    permission_query_set_append = []
    project_query_set_append = []

    for employeePermission in query_set:
                employee_query_set_append.append(employeePermission.employee)
                permission_query_set_append.append(employeePermission.permission_level)
                project_query_set_append.append(employeePermission.project)

    context = {
        'employee_object_instance' : employee_query_set_append,
        'permission_object_instance' : permission_query_set_append,
        'project_object_instance' : project_query_set_append
    }

    return render(request, 'DB3450Repo/employeePermissionAdd.html', context)

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
    project_query_set_append = []

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
                project_query_set_append.append(employeePermission.project)

    context = {
        'employee_object_instance' : employee_query_set_append,
        'permission_object_instance' : permission_query_set_append,
        'project_object_instance' : project_query_set_append
    }

    return render(request, 'DB3450Repo/employeePermission.html', context)


def employeePermissionDelete_view(request):
    query_set = EmployeePermission.objects.raw('SELECT * FROM employee_permission')
    employee_query_set = Employee.objects.raw('SELECT * FROM employee')
    permission_query_set = Permission.objects.raw('SELECT * FROM permission')
    employee_query_set_append = []
    permission_query_set_append = []
    project_query_set_append = []

    for employeePermission in query_set:
                employee_query_set_append.append(employeePermission.employee)
                permission_query_set_append.append(employeePermission.permission_level)
                project_query_set_append.append(employeePermission.project)

    context = {
        'employee_object_instance' : employee_query_set_append,
        'permission_object_instance' : permission_query_set_append,
        'project_object_instance' : project_query_set_append
    }

    return render(request, 'DB3450Repo/employeePermissionDelete.html', context)

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
    project_query_set_append = []

    for employeePermission in query_set:
                employee_query_set_append.append(employeePermission.employee)
                permission_query_set_append.append(employeePermission.permission_level)
                project_query_set_append.append(employeePermission.project)

    context = {
        'employee_object_instance' : employee_query_set_append,
        'permission_object_instance' : permission_query_set_append,
        'project_object_instance' : project_query_set_append
    }
    return render(request, 'DB3450Repo/employeePermissionAfterDelete.html', context)
  
def inventoryQuery_view(request):
    return render(request, 'DB3450Repo/inventoryQuery.html')


def inventoryDetails_view(request):
    inventory_name = request.GET['inventory_name']
    inventory_description = request.GET['inventory_description']
    query_set_append = []
    query_set = Inventory.objects.raw('SELECT * FROM inventory')
    for object in query_set:
        if(inventory_name == object.inventory_name):
            query_set_append.append(object)

    context = {
        'object_instance': query_set_append
    }

    return render(request, 'DB3450Repo/inventoryDetails.html', context)

# Add general inventory item
def inventoryAdd_view(request):
    query_set = Inventory.objects.raw('SELECT * FROM inventory')

    context = {
        'object_instance': query_set
    }
    return render(request, 'DB3450Repo/inventoryAdd.html', context)

# See results from adding inventory item
def inventoryAfterAdd_view(request):
    inventory_name_request = request.GET['inventory_name']
    inventory_description_request = request.GET['inventory_description']
    newInventory = Inventory(inventory_name=inventory_name_request,
                             inventory_description=inventory_description_request)
    newInventory.save()
    query_set_append = []
    query_set = Inventory.objects.raw('SELECT * FROM inventory')

    context = {
        'object_instance': query_set
    }

    return render(request, 'DB3450Repo/inventoryAfterAdd.html', context)


def inventoryUpdate_view(request):
    query_set = Inventory.objects.raw('SELECT * FROM inventory')

    context = {
        'object_instance': query_set
    }
    return render(request, 'DB3450Repo/inventoryUpdate.html', context)


def inventoryAfterUpdate_view(request):
    inventory_id_request = request.GET['inventory_id']
    inventory_name_request = request.GET['inventory_name']
    inventory_description_request = request.GET['inventory_description']
    # newInventory = Inventory(inventory_name = inventory_name_request, inventory_description = inventory_description_request)

    inventory_id_request_int = int(inventory_id_request)

    if(inventory_name_request == ''):
        inventory_name_request = 'none'
    if(inventory_description_request == ''):
        inventory_description_request = 'none'

    # query_set_append = []su

        # cursor = connection.cursor()
        #  cursor.execute('UPDATE inventory_supplier SET inventory_name = %s, inventory_description = %s WHERE INVENTORY_ID = %s;', [                          
        #             inventory_id_request_int, inventory_name_request, inventory_description_request])
        # cursor.close()

    newInventory = Inventory.objects.get(inventory_id=inventory_id_request)
    newInventory.inventory_name = inventory_name_request
    newInventory.inventory_description = inventory_description_request
    newInventory.save()

    query_set = Inventory.objects.raw('SELECT * FROM inventory')
    context = {
        'object_instance': query_set
    }

    return render(request, 'DB3450Repo/inventoryAfterUpdate.html', context)


def inventoryPurchaseInfo_view(request):
    query_set_append = {}
    if request.GET.get('inventory_info_id'):
        inventory_id = request.GET['inventory_info_id']
        inventory_id_int = int(inventory_id)
        cursor = connection.cursor()
        cursor.execute("""SELECT INVENTORY_NAME, PURCHASE_QUANTITY, PURCHASE_TOTAL, PURCHASE_DATE
                        FROM purchase, inventory
                        WHERE inventory.INVENTORY_ID = %s
                        AND inventory.INVENTORY_ID = purchase.INVENTORY_ID;
                        """, [inventory_id_int])
        query_set_append = cursor.fetchall()
        cursor.close()

    context = {
        'invPurchInfo': query_set_append
    }
    return render(request, 'DB3450Repo/inventoryPurchaseInfo.html', context)

def inventorySupplierView_view(request):
    query_set = InventorySupplier.objects.raw(
        'SELECT * FROM inventory_supplier')
    inventory_query_set = Inventory.objects.raw('SELECT * FROM inventory')
    supplier_query_set = SupplierCompany.objects.raw(
        'SELECT * FROM supplier_company')
    inventory_query_set_append = []
    supplier_query_set_append = []

    for inventorySupplier in query_set:
        inventory_query_set_append.append(
            inventorySupplier.inventory_supplier_inventory)
        supplier_query_set_append.append(inventorySupplier.supplier)

    context = {
        'object_instance': query_set,
        'inventory_object_instance': inventory_query_set_append,
        'supplier_object_instance': supplier_query_set_append
    }
    return render(request, 'DB3450Repo/inventorySupplierView.html', context)



def inventorySupplierAdd_view(request):
    query_set = InventorySupplier.objects.raw(
        'SELECT * FROM inventory_supplier')
    inventory_query_set = Inventory.objects.raw('SELECT * FROM inventory')
    supplier_query_set = SupplierCompany.objects.raw(
        'SELECT * FROM supplier_company')
    inventory_query_set_append = []
    supplier_query_set_append = []

    for inventorySupplier in query_set:
        inventory_query_set_append.append(
            inventorySupplier.inventory_supplier_inventory)
        supplier_query_set_append.append(inventorySupplier.supplier)

    context = {
        'object_instance': query_set,
        'inventory_object_instance': inventory_query_set_append,
        'supplier_object_instance': supplier_query_set_append
    }
    return render(request, 'DB3450Repo/inventorySupplierAddOrUpdate.html', context)


def inventorySupplierAfterAdd_view(request):
    inventory_name_request = request.GET['inventory_name']
    supplier_company_request = request.GET['supplier_company']
    inventory_supplier_cost_request = request.GET['inventory_supplier_cost']
    inventory_supplier_amount_request = request.GET['inventory_supplier_amount']
    inventory_supplier_notes_request = request.GET['inventory_supplier_notes']
    inventory_supplier_preferred_request = request.GET['inventory_supplier_preferred']

    inventory_supplier_cost_int = int(inventory_supplier_cost_request)
    inventory_supplier_amount_int = int(inventory_supplier_amount_request)
    inventory_supplier_preferred_int = int(
        inventory_supplier_preferred_request)

    final_query_set = []
    inventory_query_set_append = []
    supplier_query_set_append = []

    inventory_query_set = Inventory.objects.raw('SELECT * FROM inventory')
    supplier_query_set = SupplierCompany.objects.raw(
        'SELECT * FROM supplier_company')


    newInventory = Inventory.objects.get(inventory_name = inventory_name_request)
    newSupplier = SupplierCompany.objects.get(supplier_company_name = supplier_company_request)

    validateInventory = InventorySupplier.objects.get(inventory_supplier_inventory = newInventory, supplier = newSupplier) if InventorySupplier.objects.get(inventory_supplier_inventory = newInventory, supplier = newSupplier) is not None else None

    if(validateInventory is not None):
        cursor = connection.cursor()
        cursor.execute('UPDATE inventory_supplier SET inventory_supplier_cost = %s, inventory_supplier_amount = %s, inventory_supplier_notes = %s, inventory_supplier_preferred = %s WHERE INVENTORY_SUPPLIER_INVENTORY_ID = %s AND SUPPLIER_ID = %s', [
                       inventory_supplier_cost_int, inventory_supplier_amount_int, inventory_supplier_notes_request, inventory_supplier_preferred_int, validateInventory.inventory_supplier_inventory.inventory_id, validateInventory.supplier.supplier_company_id])

    if((newInventory is not None or newSupplier is not None) and validateInventory is None):
        newInventorySupplier = InventorySupplier(inventory_supplier_inventory=newInventory, supplier=newSupplier, inventory_supplier_cost=inventory_supplier_cost_request,
                                                 inventory_supplier_amount=inventory_supplier_amount_request, inventory_supplier_notes=inventory_supplier_notes_request, inventory_supplier_preferred=inventory_supplier_preferred_request)
        cursor = connection.cursor()
        cursor.execute('INSERT INTO inventory_supplier VALUES (%s,%s,%s,%s,%s,%s)', [
                       newInventory.inventory_id, newSupplier.supplier_company_id, inventory_supplier_cost_int, inventory_supplier_amount_int, inventory_supplier_notes_request, inventory_supplier_preferred_int])
        connection.commit()

    query_set = InventorySupplier.objects.raw(
        'SELECT * FROM inventory_supplier')

    for inventorySupplier in query_set:
        inventory_query_set_append.append(
            inventorySupplier.inventory_supplier_inventory)
        supplier_query_set_append.append(inventorySupplier.supplier)

    context = {
        'object_instance': query_set,
        'inventory_object_instance': inventory_query_set_append,
        'supplier_object_instance': supplier_query_set_append
    }

    return render(request, 'DB3450Repo/inventorySupplierAfterAddOrUpdate.html', context)


def inventorySupplierDelete_view(request):
    query_set = InventorySupplier.objects.raw(
        'SELECT * FROM inventory_supplier')
    inventory_query_set = Inventory.objects.raw('SELECT * FROM inventory')
    supplier_query_set = SupplierCompany.objects.raw(
        'SELECT * FROM supplier_company')
    inventory_query_set_append = []
    supplier_query_set_append = []

    for inventorySupplier in query_set:
        inventory_query_set_append.append(
            inventorySupplier.inventory_supplier_inventory)
        supplier_query_set_append.append(inventorySupplier.supplier)

    context = {
        'object_instance': query_set,
        'inventory_object_instance': inventory_query_set_append,
        'supplier_object_instance': supplier_query_set_append
    }
    return render(request, 'DB3450Repo/inventorySupplierDelete.html', context)


def inventorySupplierAfterDelete_view(request):
    inventory_name_request = request.GET['inventory_name']
    supplier_company_request = request.GET['supplier_company']
    final_query_set = []
    inventory_query_set_append = []
    supplier_query_set_append = []

    inventory_query_set = Inventory.objects.raw('SELECT * FROM inventory')
    supplier_query_set = SupplierCompany.objects.raw(
        'SELECT * FROM supplier_company')

    newInventory = Inventory.objects.get(inventory_name=inventory_name_request)
    newSupplier = SupplierCompany.objects.get(
        supplier_company_name=supplier_company_request)

    validateInventory = InventorySupplier.objects.get(
        inventory_supplier_inventory=newInventory, supplier=newSupplier)
    cursor = connection.cursor()
    cursor.execute('DELETE FROM inventory_supplier WHERE INVENTORY_SUPPLIER_INVENTORY_ID = %s AND SUPPLIER_ID = %s', [
                   newInventory.inventory_id, newSupplier.supplier_company_id])
    connection.commit()

    query_set = InventorySupplier.objects.raw(
        'SELECT * FROM inventory_supplier')

    for inventorySupplier in query_set:
        inventory_query_set_append.append(
            inventorySupplier.inventory_supplier_inventory)
        supplier_query_set_append.append(inventorySupplier.supplier)

    context = {
        'object_instance': query_set,
        'inventory_object_instance': inventory_query_set_append,
        'supplier_object_instance': supplier_query_set_append
    }

    return render(request, 'DB3450Repo/inventorySupplierAfterDelete.html', context)

# EMPLOYEE LINK HANDLING
def employeeLanding_view(request):
    return render(request, 'DB3450Repo/employeeLanding.html')

def employeePurchaseInfo_view(request):
    query_set_append = {}
    if request.GET.get('employee_info_id'):
        employee_id = request.GET['employee_info_id']
        employee_id_int = int(employee_id)
        cursor = connection.cursor()
        cursor.execute("""SELECT INVENTORY_NAME, PURCHASE_QUANTITY, PURCHASE_TOTAL, PURCHASE_DATE
                          FROM purchase, inventory
                          WHERE purchase.EMPLOYEE_ID = %s
                          AND purchase.INVENTORY_ID = inventory.INVENTORY_ID;
                        """, [employee_id_int])
        query_set_append = cursor.fetchall()
        cursor.close()
    print(query_set_append)
    return render(request, 'DB3450Repo/employeePurchaseInfo.html', {'empPurchInfo': query_set_append})

def employeePermission_view(request):
    query_set = EmployeePermission.objects.raw(
        'SELECT * FROM employee_permission')
    employee_query_set = Employee.objects.raw('SELECT * FROM employee')
    permission_query_set = Permission.objects.raw('SELECT * FROM permission')
    employee_query_set_append = []
    permission_query_set_append = []
    project_query_set_append = []

    for employeePermission in query_set:
        employee_query_set_append.append(employeePermission.employee)
        permission_query_set_append.append(employeePermission.permission_level)
        project_query_set_append.append(employeePermission.project)

    context = {
        'employee_object_instance': employee_query_set_append,
        'permission_object_instance': permission_query_set_append,
        'project_object_instance' : project_query_set_append
    }
    return render(request, 'DB3450Repo/employeePermission.html', context)

def employeePermissionAdd_view(request):
    query_set = EmployeePermission.objects.raw(
        'SELECT * FROM employee_permission')
    employee_query_set = Employee.objects.raw('SELECT * FROM employee')
    permission_query_set = Permission.objects.raw('SELECT * FROM permission')
    employee_query_set_append = []
    permission_query_set_append = []
    project_query_set_append = []

    for employeePermission in query_set:
        employee_query_set_append.append(employeePermission.employee)
        permission_query_set_append.append(employeePermission.permission_level)
        project_query_set_append.append(employeePermission.project)

    context = {
        'employee_object_instance': employee_query_set_append,
        'permission_object_instance': permission_query_set_append,
        'project_object_instance' : project_query_set_append
    }

    return render(request, 'DB3450Repo/employeePermissionAdd.html', context)


def employeePermissionAfterAdd_view(request):
    employee_id = request.GET['employee_id']
    permission_level = request.GET['permission_level']
    project_id = request.GET['project_id']
    employee_permission_start = request.GET['start_date']

    validEmployee = Employee.objects.get(employee_id=employee_id)
    validPermission = Permission.objects.get(permission_level=permission_level)
    validProject = Project.objects.get(project_id=project_id)

    query_set_append = []
    query_set = EmployeePermission.objects.raw(
        'SELECT * FROM employee_permission')
    new_query_set = query_set
    employee_query_set = Employee.objects.raw('SELECT * FROM employee')
    permission_query_set = Permission.objects.raw('SELECT * FROM permission')
    project_query_set = Project.objects.raw('SELECT * FROM project')
    employee_query_set_append = []
    permission_query_set_append = []
    project_query_set_append = []

    x = 0

    for object in query_set:
        query_set_append.append(object)
        if(validEmployee == object.employee and validPermission == object.permission_level and validProject == object.project):
            x += 1

    if(x == 0):
        newEmployeePermission = EmployeePermission(employee_id=validEmployee.employee_id, permission_level=validPermission,
                                                   project_id=project_id, employee_permission_start=employee_permission_start)
        newEmployeePermission.save()
        new_query_set = EmployeePermission.objects.raw(
            'SELECT * FROM employee_permission')
        # EmployeePermission.INSERT('INSERT INTO employee_permission (employee_id, permission_level, project_id, employee_permission_start)' 'VALUES (%s, %s, %s, %s),' [employee_id, permission_level, project_id, employee_permission_start])
        # new_query_set = EmployeePermission.objects.raw('SELECT * FROM employee_permission')

    employee_query_set_final = Employee.objects.raw('SELECT * FROM employee')
    permission_query_set_final = Permission.objects.raw(
        'SELECT * FROM permission')

    for employeePermission in new_query_set:
        employee_query_set_append.append(employeePermission.employee)
        permission_query_set_append.append(employeePermission.permission_level)
        project_query_set_append.append(employeePermission.project)

    context = {
        'employee_object_instance': employee_query_set_append,
        'permission_object_instance': permission_query_set_append,
        'project_object_instance': project_query_set_append
    }

    return render(request, 'DB3450Repo/employeePermission.html', context)

def employeePermissionQuery_view(request):
    return render(request, 'DB3450Repo/employeePermissionQuery.html')


def employeePermissionDetails_view(request):
    employee_id_request = request.GET['employee_id']

    query_set = EmployeePermission.objects.raw(
        'SELECT * FROM employee_permission')
    employee_query_set = Employee.objects.raw('SELECT * FROM employee')
    permission_query_set = Permission.objects.raw('SELECT * FROM permission')

    employee_query_set_append = []
    permission_query_set_append = []
    project_query_set_append = []

    validEmployee = Employee.objects.get(employee_id=employee_id_request)

    for employeePermission in query_set:
        if(employeePermission.employee == validEmployee):
            employee_query_set_append.append(employeePermission.employee)
            permission_query_set_append.append(
                employeePermission.permission_level)

    context = {
        'employee_object_instance': employee_query_set_append,
        'permission_object_instance': permission_query_set_append,
        'project_object_instance': project_query_set_append
    }

    return render(request, 'DB3450Repo/employeePermissionDetails.html', context)

def employeePermissionDelete_view(request):
    query_set = EmployeePermission.objects.raw(
        'SELECT * FROM employee_permission')
    employee_query_set = Employee.objects.raw('SELECT * FROM employee')
    permission_query_set = Permission.objects.raw('SELECT * FROM permission')
    employee_query_set_append = []
    permission_query_set_append = []
    project_query_set_append = []

    for employeePermission in query_set:
        employee_query_set_append.append(employeePermission.employee)
        permission_query_set_append.append(employeePermission.permission_level)
        project_query_set_append.append(employeePermission.project)

    context = {
        'employee_object_instance': employee_query_set_append,
        'permission_object_instance': permission_query_set_append,
        'project_object_instance': project_query_set_append
    }

    return render(request, 'DB3450Repo/employeePermissionDelete.html', context)


def employeePermissionAfterDelete_view(request):
    employee_id = request.GET['employee_id']
    permission_level = request.GET['permission_level']
    project_id = request.GET['project_id']
    employee_permission_start = date.today()

    validEmployee = Employee.objects.get(employee_id=employee_id)
    validPermission = Permission.objects.get(permission_level=permission_level)
    validProject = Project.objects.get(project_id=project_id)

    query_set = EmployeePermission.objects.raw(
        'SELECT * FROM employee_permission')

    for employeePermission in query_set:
        if(employeePermission.employee == validEmployee and employeePermission.permission_level == validPermission and employeePermission.project == validProject):
            employeePermission.delete()

    new_query_set = EmployeePermission.objects.raw(
        'SELECT * FROM employee_permission')
    employee_query_set_final = Employee.objects.raw('SELECT * FROM employee')
    permission_query_set_final = Permission.objects.raw(
        'SELECT * FROM permission')
    employee_query_set_append = []
    permission_query_set_append = []

    for employeePermission in new_query_set:
        employee_query_set_append.append(employeePermission.employee)
        permission_query_set_append.append(employeePermission.permission_level)

    context = {
        'employee_object_instance': employee_query_set_append,
        'permission_object_instance': permission_query_set_append
    }
    return render(request, 'DB3450Repo/employeePermissionAfterDelete.html', context)

def employeeHoursQuery_view(request):
    return render(request, 'DB3450Repo/employeeHoursQuery.html')

def employeeHoursDetails_view(request):
    employee_id_request = request.GET['employee_id']
    start_date_request = request.GET['start_date']

    employee_name = Employee.objects.raw(
        'SELECT * FROM employee WHERE employee_id=' + employee_id_request)
    employee_hours_query_set = EmployeeHours.objects.raw(
        'SELECT * FROM employee_hours WHERE employee_id=' + employee_id_request + ' AND employee_hours_first_day="' + start_date_request + '"')

    project_list = []
    mon1_list = []
    tues1_list = []
    wed1_list = []
    thur1_list = []
    fri1_list = []
    sat1_list = []
    sun1_list = []
    mon2_list = []
    tues2_list = []
    wed2_list = []
    thur2_list = []
    fri2_list = []
    sat2_list = []
    sun2_list = []

    for employeeHours in employee_hours_query_set:
        project_list.append(employeeHours.project_id)
        mon1_list.append(employeeHours.employee_hours_mon1)
        tues1_list.append(employeeHours.employee_hours_tue1)
        wed1_list.append(employeeHours.employee_hours_wed1)
        thur1_list.append(employeeHours.employee_hours_thr1)
        fri1_list.append(employeeHours.employee_hours_fri1)
        sat1_list.append(employeeHours.employee_hours_sat1)
        sun1_list.append(employeeHours.employee_hours_sun1)
        mon2_list.append(employeeHours.employee_hours_mon2)
        tues2_list.append(employeeHours.employee_hours_tue2)
        wed2_list.append(employeeHours.employee_hours_wed2)
        thur2_list.append(employeeHours.employee_hours_thr2)
        fri2_list.append(employeeHours.employee_hours_fri2)
        sat2_list.append(employeeHours.employee_hours_sat2)
        sun2_list.append(employeeHours.employee_hours_sun2)

    context = {
        'employee_name': employee_name,
        'start_date': [start_date_request],
        'project_list': project_list,
        'mon1_list': mon1_list,
        'tues1_list': tues1_list,
        'wed1_list': wed1_list,
        'thur1_list': thur1_list,
        'fri1_list': fri1_list,
        'sat1_list': sat1_list,
        'sun1_list': sun1_list,
        'mon2_list': mon2_list,
        'tues2_list': tues2_list,
        'wed2_list': wed2_list,
        'thur2_list': thur2_list,
        'fri2_list': fri2_list,
        'sat2_list': sat2_list,
        'sun2_list':  sun2_list,
    }
    return render(request, 'DB3450Repo/employeeHoursDetails.html', context)


def employeeHoursAdd_view(request):
    employee_id_request = request.GET.get('employee_id')
    project_id_request = request.GET.get('project_id')
    start_date_request = request.GET.get('start_date')
    mon1 = request.GET.get('mon1')
    tues1 = request.GET.get('tues1')
    wed1 = request.GET.get('wed1')
    thur1 = request.GET.get('thur1')
    fri1 = request.GET.get('fri1')
    sat1 = request.GET.get('sat1')
    sun1 = request.GET.get('sun2')
    mon2 = request.GET.get('mon2')
    tues2 = request.GET.get('tues2')
    wed2 = request.GET.get('wed2')
    thur2 = request.GET.get('thur2')
    fri2 = request.GET.get('fri2')
    sat2 = request.GET.get('sat2')
    sun2 = request.GET.get('sun2')

    messages = []

    if employee_id_request == "" or start_date_request == "" or employee_id_request == None or start_date_request == None:
        messages.append(
            "Enter an employee id, start date, and the other necessary information to log time worked")
    else:
        previous_records = []
        if project_id_request != "":
            previous_records = EmployeeHours.objects.raw(
                'SELECT * FROM employee_hours WHERE employee_id=' + employee_id_request + ' AND employee_hours_first_day="' + start_date_request + '" AND project_id=' + project_id_request)
        else:
            previous_records = EmployeeHours.objects.raw(
                'SELECT * FROM employee_hours WHERE employee_id=' + employee_id_request + ' AND employee_hours_first_day="' + start_date_request + '" AND project_id IS NULL')

        count = 0
        for record in previous_records:
            count = count + 1

        if count > 0:
            messages.append(
                "You have already logged your time for this project for this pay period. If you need to fix this time sheet, please contact your manager.")
        else:
            employee_pay_rate = Employee.objects.raw(
                'SELECT * FROM employee WHERE employee_id=' + employee_id_request)[0].employee_pay_rate

            sql = 'INSERT INTO employee_hours SET employee_id=' + employee_id_request + \
                ', employee_hours_first_day="' + start_date_request + \
                '", employee_hours_rate=' + str(employee_pay_rate)
            if (project_id_request != ""):
                sql = sql + ", project_id=" + project_id_request
            # Monday 1
            if (mon1 != ""):
                sql = sql + ", employee_hours_mon1=" + mon1
            else:
                sql = sql + ", employee_hours_mon1=0"
            # Tuesday 1
            if (tues1 != ""):
                sql = sql + ", employee_hours_tue1=" + tues1
            else:
                sql = sql + ", employee_hours_tue1=0"
            # Wednesday 1
            if (wed1 != ""):
                sql = sql + ", employee_hours_wed1=" + wed1
            else:
                sql = sql + ", employee_hours_wed1=0"
            # Thursday 1
            if (thur1 != ""):
                sql = sql + ", employee_hours_thr1=" + thur1
            else:
                sql = sql + ", employee_hours_thr1=0"
            # Friday 1
            if (fri1 != ""):
                sql = sql + ", employee_hours_fri1=" + fri1
            else:
                sql = sql + ", employee_hours_fri1=0"
            # Saturday 1
            if (sat1 != ""):
                sql = sql + ", employee_hours_sat1=" + sat1
            else:
                sql = sql + ", employee_hours_sat1=0"
            # Sunday 1
            if (sun1 != ""):
                sql = sql + ", employee_hours_sun1=" + sun1
            else:
                sql = sql + ", employee_hours_sun1=0"
            # Monday 2
            if (mon2 != ""):
                sql = sql + ", employee_hours_mon2=" + mon2
            else:
                sql = sql + ", employee_hours_mon2=0"
            # Tuesday 2
            if (tues2 != ""):
                sql = sql + ", employee_hours_tue2=" + tues2
            else:
                sql = sql + ", employee_hours_tue2=0"
            # Wednesday 2
            if (wed2 != ""):
                sql = sql + ", employee_hours_wed2=" + wed2
            else:
                sql = sql + ", employee_hours_wed2=0"
            # Thursday 2
            if (thur2 != ""):
                sql = sql + ", employee_hours_thr2=" + thur2
            else:
                sql = sql + ", employee_hours_thr2=0"
            # Friday 2
            if (fri2 != ""):
                sql = sql + ", employee_hours_fri2=" + fri2
            else:
                sql = sql + ", employee_hours_fri2=0"
            # Saturday 2
            if (sat2 != ""):
                sql = sql + ", employee_hours_sat2=" + sat2
            else:
                sql = sql + ", employee_hours_sat2=0"
            # Sunday 2
            if (sun2 != ""):
                sql = sql + ", employee_hours_sun2=" + sun2 + ";"
            else:
                sql = sql + ", employee_hours_sun2=0;"
            print(sql)
            django.db.connection.cursor().execute(sql)
            messages = ["Hours logged successfully!"]

    context = {
        'messages': messages
    }
    return render(request, 'DB3450Repo/employeeHoursAdd.html', context)


def employeeHoursEdit_view(request):
    employee_id_request = request.GET.get('employee_id')
    project_id_request = request.GET.get('project_id')
    start_date_request = request.GET.get('start_date')

    previous_records = []
    if project_id_request != "":
        previous_records = EmployeeHours.objects.raw(
            'SELECT * FROM employee_hours WHERE employee_id=' + employee_id_request + ' AND employee_hours_first_day="' + start_date_request + '" AND project_id=' + project_id_request)
    else:
        previous_records = EmployeeHours.objects.raw(
            'SELECT * FROM employee_hours WHERE employee_id=' + employee_id_request + ' AND employee_hours_first_day="' + start_date_request + '" AND project_id IS NULL')

    if len(previous_records) > 0:
        return render(request, 'DB3450Repo/employeeHoursEdit.html', {
            'employee_hours': [previous_records[0]]
        })
    else:
        return render(request, 'DB3450Repo/employeeHoursEditSelect.html', {'messages': ["No Timesheet Found with those parameters."]})

def employeeHoursEditSelect_view(request):
    employee_id_request = request.GET.get('employee_id')
    project_id_request = request.GET.get('project_id')
    start_date_request = request.GET.get('start_date')
    mon1 = request.GET.get('mon1')
    tues1 = request.GET.get('tues1')
    wed1 = request.GET.get('wed1')
    thur1 = request.GET.get('thur1')
    fri1 = request.GET.get('fri1')
    sat1 = request.GET.get('sat1')
    sun1 = request.GET.get('sun2')
    mon2 = request.GET.get('mon2')
    tues2 = request.GET.get('tues2')
    wed2 = request.GET.get('wed2')
    thur2 = request.GET.get('thur2')
    fri2 = request.GET.get('fri2')
    sat2 = request.GET.get('sat2')
    sun2 = request.GET.get('sun2')

    messages = []

    if employee_id_request == "" or start_date_request == "" or employee_id_request == None or start_date_request == None:
        messages.append(
            "Enter an employee id, start date, and the other necessary project id if required to update an employee's hours.")
    else:
        sql = 'UPDATE employee_hours SET '
        # Monday 1
        if (mon1 != ""):
            sql = sql + "employee_hours_mon1=" + mon1
        else:
            sql = sql + "employee_hours_mon1=0"
        # Tuesday 1
        if (tues1 != ""):
            sql = sql + ", employee_hours_tue1=" + tues1
        else:
            sql = sql + ", employee_hours_tue1=0"
        # Wednesday 1
        if (wed1 != ""):
            sql = sql + ", employee_hours_wed1=" + wed1
        else:
            sql = sql + ", employee_hours_wed1=0"
        # Thursday 1
        if (thur1 != ""):
            sql = sql + ", employee_hours_thr1=" + thur1
        else:
            sql = sql + ", employee_hours_thr1=0"
        # Friday 1
        if (fri1 != ""):
            sql = sql + ", employee_hours_fri1=" + fri1
        else:
            sql = sql + ", employee_hours_fri1=0"
        # Saturday 1
        if (sat1 != ""):
            sql = sql + ", employee_hours_sat1=" + sat1
        else:
            sql = sql + ", employee_hours_sat1=0"
        # Sunday 1
        if (sun1 != ""):
            sql = sql + ", employee_hours_sun1=" + sun1
        else:
            sql = sql + ", employee_hours_sun1=0"
        # Monday 2
        if (mon2 != ""):
            sql = sql + ", employee_hours_mon2=" + mon2
        else:
            sql = sql + ", employee_hours_mon2=0"
        # Tuesday 2
        if (tues2 != ""):
            sql = sql + ", employee_hours_tue2=" + tues2
        else:
            sql = sql + ", employee_hours_tue2=0"
        # Wednesday 2
        if (wed2 != ""):
            sql = sql + ", employee_hours_wed2=" + wed2
        else:
            sql = sql + ", employee_hours_wed2=0"
        # Thursday 2
        if (thur2 != ""):
            sql = sql + ", employee_hours_thr2=" + thur2
        else:
            sql = sql + ", employee_hours_thr2=0"
        # Friday 2
        if (fri2 != ""):
            sql = sql + ", employee_hours_fri2=" + fri2
        else:
            sql = sql + ", employee_hours_fri2=0"
        # Saturday 2
        if (sat2 != ""):
            sql = sql + ", employee_hours_sat2=" + sat2
        else:
            sql = sql + ", employee_hours_sat2=0"
        # Sunday 2
        if (sun2 != ""):
            sql = sql + ", employee_hours_sun2=" + sun2
        else:
            sql = sql + ", employee_hours_sun2=0"
        sql = sql + ' WHERE employee_id=' + employee_id_request + \
            ' AND employee_hours_first_day="' + \
            datetime.strptime(start_date_request,
                              '%B %d, %Y').isoformat()[0:10] + '"'
        if (project_id_request != None and project_id_request != "" and project_id_request != "None"):
            sql = sql + " AND project_id=" + project_id_request
        sql = sql + ";"
        print(sql)
        django.db.connection.cursor().execute(sql)
        messages = ["Hours updated successfully!"]

    context = {
        'messages': messages
    }
    return render(request, 'DB3450Repo/employeeHoursEditSelect.html', context)


def employeeEmployeesManaged_view(request):
    employee_id_request = request.GET.get('employee_id')
    print(employee_id_request)

    query_results = []
    if (employee_id_request != None and employee_id_request != ""):
        query_results = Employee.objects.raw(
            'SELECT * FROM employee WHERE employee_manager_id=' + employee_id_request + ";")

    context = {
        'employees': query_results
    }
    return render(request, 'DB3450Repo/employeeEmployeesManaged.html', context)


def employeeCustomersManaged_view(request):
    employee_id_request = request.GET.get('employee_id')
    print(employee_id_request)

    query_results = []
    if (employee_id_request != None and employee_id_request != ""):
        query_results = CustomerCompany.objects.raw(
            'SELECT * FROM customer_company WHERE employee_id=' + employee_id_request + ";")

    context = {
        'customers': query_results
    }
    return render(request, 'DB3450Repo/employeeCustomersManaged.html', context)


def employeeAdd_view(request):
    first_name = request.GET.get('first_name')
    middle_name = request.GET.get('middle_name')
    last_name = request.GET.get('last_name')
    title = request.GET.get('title')
    dob = request.GET.get('dob')
    hire_date = request.GET.get('hire_date')
    work_email = request.GET.get('work_email')
    alt_email = request.GET.get('alt_email')
    work_phone = request.GET.get('work_phone')
    alt_phone = request.GET.get('alt_phone')
    manager_id = request.GET.get('manager_id')
    pay_rate = request.GET.get('pay_rate')

    messages = []

    if first_name == "" or middle_name == "" or last_name == "" or title == "" or dob == "" or hire_date == "" or work_email == "" or alt_email == "" or work_phone == "" or alt_phone == "" or manager_id == "" or pay_rate == "" or first_name == None or middle_name == None or last_name == None or title == None or dob == None or hire_date == None or work_email == None or alt_email == None or work_phone == None or alt_phone == None or manager_id == None or pay_rate == None:
        messages.append(
            "Enter the other necessary information to add an employee")
    else:
        sql = "INSERT INTO employee SET employee_name_first=\"" + first_name + "\", employee_name_middle=\"" + middle_name + "\", employee_name_last=\"" + last_name + "\", employee_title=\"" + title + "\", employee_dob=\"" + dob + \
            ", employee_hire_date=\"" + hire_date + "\", employee_email_work=\"" + work_email + "\", employee_email_alt=\"" + alt_email + \
            "\", employee_tel_work=" + work_phone + ", employee_tel_alt=" + \
            alt_phone + ", employee_pay_rate=" + pay_rate
        if (manager_id != "" and manager_id != None):
            sql = sql + ", employee_manager_id=" + manager_id
        sql = sql + ";"
        print(sql)
        django.db.connection.cursor().execute(sql)
        messages = ["Employee Added successfully!"]

    context = {
        'messages': messages
    }
    return render(request, 'DB3450Repo/employeeAdd.html', context)


def employeeUpdate_view(request):
    first_name = request.GET.get('first_name')
    middle_name = request.GET.get('middle_name')
    last_name = request.GET.get('last_name')
    title = request.GET.get('title')
    dob = request.GET.get('dob')
    hire_date = request.GET.get('hire_date')
    work_email = request.GET.get('work_email')
    alt_email = request.GET.get('alt_email')
    work_phone = request.GET.get('work_phone')
    alt_phone = request.GET.get('alt_phone')
    manager_id = request.GET.get('manager_id')
    pay_rate = request.GET.get('pay_rate')

    messages = []

    if first_name == "" or middle_name == "" or last_name == "" or title == "" or dob == "" or hire_date == "" or work_email == "" or alt_email == "" or work_phone == "" or alt_phone == "" or manager_id == "" or pay_rate == "" or first_name == None or middle_name == None or last_name == None or title == None or dob == None or hire_date == None or work_email == None or alt_email == None or work_phone == None or alt_phone == None or manager_id == None or pay_rate == None:
        messages.append(
            "Enter the other necessary information to add an employee")
    else:
        sql = "INSERT INTO employee SET employee_name_first=\"" + first_name + "\", employee_name_middle=\"" + middle_name + "\", employee_name_last=\"" + last_name + "\", employee_title=\"" + title + "\", employee_dob=\"" + dob + \
            "\", employee_hire_date=\"" + hire_date + "\", employee_email_work=\"" + work_email + "\", employee_email_alt=\"" + alt_email + \
            ", employee_tel_work" + work_phone + ", employee_tel_alt" + \
            alt_phone + ", employee_pay_rate=" + pay_rate
        if (manager_id != "" and manager_id != None):
            sql = sql + ", employee_manager_id=" + manager_id
        sql = sql + ";"
        print(sql)
        django.db.connection.cursor().execute(sql)
        messages = ["Employee Added successfully!"]

    context = {
        'messages': messages
    }
    return render(request, 'DB3450Repo/employeeUpdate.html', context)


def employeeDelete_view(request):
    return render(request, 'DB3450Repo/employeeDelete.html')


def employeeHome_view(request):
    return render(request, 'DB3450Repo/employeeHome.html')


def employeeHoursHome_view(request):
    return render(request, 'DB3450Repo/employeeHoursHome.html')

# SUPPLIER LINK HANDLING
def supplierLanding_view(request):
    return render(request, 'DB3450Repo/supplierLanding.html')


def supplierAddOrUpdate_view(request):
    query_set = SupplierCompany.objects.raw('SELECT * FROM supplier_company')

    context = {
        'object_instance': query_set,
    }
    return render(request, 'DB3450Repo/supplierAddOrUpdate.html', context)

def supplierView_view(request):
    query_set = SupplierCompany.objects.raw('SELECT * FROM supplier_company')

    context = {
        'object_instance': query_set,
    }
    return render(request, 'DB3450Repo/supplierView.html', context)



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
        validateSupplier = SupplierCompany.objects.get(
            supplier_company_id=id_req_int)
    else:
        validateSupplier = None

    if(validateSupplier is not None):
        cursor = connection.cursor()
        cursor.execute('UPDATE supplier_company SET supplier_company_name = %s, supplier_company_street1 = %s, supplier_company_street2 = %s, supplier_company_city = %s, supplier_company_state = %s, supplier_company_zip = %s, supplier_company_notes = %s WHERE SUPPLIER_COMPANY_ID = %s', [
                       name_req, streetOne_req, streetTwo_req, city_req, state_req, zip_req, notes_req, id_req_int])
        connection.commit()

    if(validateSupplier is None):
        cursor = connection.cursor()
        cursor.execute('INSERT INTO supplier_company (supplier_company_name, supplier_company_street1, supplier_company_street2, supplier_company_city, supplier_company_state, supplier_company_zip, supplier_company_notes) VALUES (%s,%s,%s,%s,%s,%s,%s)', [
                       name_req, streetOne_req, streetTwo_req, city_req, state_req, zip_req, notes_req])
        connection.commit()

    query_set = SupplierCompany.objects.raw('SELECT * FROM supplier_company')

    context = {
        'object_instance': query_set,
    }
    return render(request, 'DB3450Repo/supplierAfterAddOrUpdate.html', context)


def supplierContactUpdate_view(request):
    query_set = SupplierContact.objects.raw('SELECT * FROM supplier_contact')

    context = {
        'object_instance': query_set,
    }
    return render(request, 'DB3450Repo/supplierContactUpdate.html', context)


def supplierContactAfterUpdate_view(request):
    id_req = request.GET['supplier_contact_id']
    id2_req = request.GET['supplier_id']
    fname_req = request.GET['supplier_contact_fname']
    lname_req = request.GET['supplier_contact_lname']
    email_req = request.GET['supplier_contact_email']
    tel_req = request.GET['supplier_contact_tel']
    role_req = request.GET['supplier_contact_role']
    current_req = request.GET['supplier_contact_current']
    id_req_int = 0
    validateSupplier = None

    if(id_req is not None and id_req != ''):
        id_req_int = int(id_req)
        id2_req_int = int(id2_req)
        validateSupplier = SupplierContact.objects.get(
            supplier_contact_id=id_req_int)
    else:
        validateSupplier = None

    if(validateSupplier is not None):
        cursor = connection.cursor()
        cursor.execute('UPDATE supplier_contact SET supplier_contact_fname = %s, supplier_contact_lname = %s, supplier_contact_email = %s, supplier_contact_tel = %s, supplier_contact_role = %s, supplier_contact_current = %s WHERE SUPPLIER_COMPANY_ID = %s', [
                       fname_req, lname_req, email_req, tel_req, role_req, current_req])
        connection.commit()

    query_set = SupplierContact.objects.raw('SELECT * FROM supplier_contact')

    context = {
        'object_instance': query_set,
    }
    return render(request, 'DB3450Repo/supplierContactAfterUpdate.html', context)

def supplierCompanyDelete_view(request):
    if request.GET.get('supplier_com_del_id'):
        supplier_company_id_req = request.GET['supplier_com_del_id']
        supplier_int = int(supplier_company_id_req)
        cursor = connection.cursor()
        cursor.execute("DELETE FROM supplier_company WHERE SUPPLIER_COMPANY_ID = %s ", [supplier_int])
        connection.commit()

    return render(request, 'DB3450Repo/supplierCompanyDelete.html')

def supplierContactDelete_views(request):
    if request.GET.get('supplier_con_del_id'):
        supplier_contact_id_req = request.GET['supplier_con_del_id']
        supplier_int = int(supplier_contact_id_req)
        cursor = connection.cursor()
        cursor.execute("UPDATE supplier_contact SET SUPPLIER_CONTACT_CURRENT = %s WHERE SUPPLIER_CONTACT_ID = %s ", [1, supplier_int])
        connection.commit()

    return render(request, 'DB3450Repo/supplierContactDelete.html')

# PROJECT LINK HANDLING
# Retrieve the project name and status
def projectBaseInfo_view(request):
    query_set_append = []
    if request.GET.get('project_id'):
        project_id = request.GET['project_id']
        project_id_int = int(project_id)
        # Creating session variable
        request.session['project_id'] = project_id_int
        query_set = Project.objects.raw('SELECT * FROM project')
        for object in query_set:
            if(project_id_int == object.project_id):
                query_set_append.append(object)

    context = {
        'project_details': query_set_append
    }

    return render(request, 'DB3450Repo/projectBaseInfo.html', context)

def inventoryBaseInfo_view(request):
    return render(request, 'DB3450Repo/inventoryBaseInfo.html')


# Add a new project 
def projectadd_view(request):
    if request.GET.get('project_add_id'):
        project_id = request.GET['project_add_id']
        project_id_int = int(project_id)
        project_status = request.GET['project_add_status']
        project_name = request.GET['project_add_name']
        project_budget = request.GET['project_add_budget']
        project_budget_dec = float(project_budget)
        customer_company_id = request.GET['cus_comp_add_id']
        customer_company_id_int = int(customer_company_id)
        cursor = connection.cursor()
        cursor.execute("INSERT INTO project VALUES(%s,%s,%s,%s,%s)", [
                       project_id_int, project_status, project_name, project_budget_dec, customer_company_id_int])
        connection.commit()
        cursor.close()

    return render(request, 'DB3450Repo/projectAdd.html')

# Retrieve the project budget and expenditure information
def projectBudget_view(request):
    project_id_int = request.session.get('project_id')
    query_set_append = []
    query_set = Project.objects.raw('SELECT * FROM project')
    # Get budget total for project
    for object in query_set:
        if(project_id_int == object.project_id):
            query_set_append.append(object)

    # Get purchase information for the project
    cursor = connection.cursor()
    cursor.execute("""SELECT INVENTORY_NAME, PURCHASE_TOTAL, PURCHASE_QUANTITY, PURCHASE_DATE
                      FROM purchase JOIN inventory using (INVENTORY_ID)
                      WHERE project_id = %s;
                   """, [project_id_int])
    purchaseProjectInformation = cursor.fetchall()

    # Get employee hours information
    cursor.execute("""SELECT EMPLOYEE_ID, EMPLOYEE_NAME_FIRST, EMPLOYEE_NAME_LAST, SUM(EMPLOYEE_HOURS_RATE * (EMPLOYEE_HOURS_SUN1 + EMPLOYEE_HOURS_MON1 + EMPLOYEE_HOURS_TUE1 + EMPLOYEE_HOURS_WED1 + EMPLOYEE_HOURS_THR1 + EMPLOYEE_HOURS_FRI1 + EMPLOYEE_HOURS_SAT1 + 
                      EMPLOYEE_HOURS_SUN2 + EMPLOYEE_HOURS_MON2 + EMPLOYEE_HOURS_TUE2 + EMPLOYEE_HOURS_WED2 + EMPLOYEE_HOURS_THR2 + EMPLOYEE_HOURS_FRI2 + EMPLOYEE_HOURS_SAT2))
                      FROM employee JOIN employee_hours USING (EMPLOYEE_ID)
                      WHERE project_id = %s
                      GROUP BY EMPLOYEE_ID;
                   """, [project_id_int])
    employeeCostInformation = cursor.fetchall()
    
    context = {
        'budgetResults': query_set_append,
        'purchaseProjectInfo': purchaseProjectInformation,
        'employeeCostInfo': employeeCostInformation,
    }

    return render(request, 'DB3450Repo/projectBudget.html', context)

# Retrieve project employee information
def projectEmployees_view(request):
    project_id_int = request.session.get('project_id')
    cursor = connection.cursor()
    # Despite what is says here, it gets the first name first and last name second
    cursor.execute("""SELECT employee_name_last, employee_name_first
                      FROM employee  
                      WHERE employee_id in (
                          SELECT employee_id
                          FROM employee_permission
                          WHERE project_id = %s
                      );
                        """, [project_id_int])
    query_set_append = cursor.fetchall()
    cursor.close()

    return render(request, 'DB3450Repo/projectEmployees.html', {'projectEmployees': query_set_append})

# Retrieve information about inventory items belonging to the project
def projectInventory_view(request):
    project_id_int = request.session.get('project_id')
    cursor = connection.cursor()

    # Despite this being a delete method, we're really updating the quantity value in project_inventory
    if request.GET.get('inventory_item_name_delete'):
        inventory_name_delete = request.GET['inventory_item_name_delete']
        quantity_amount_delete = request.GET['quantity_delete']
        quantity_amount_delete_int = int(quantity_amount_delete)

        # Match inventory name with inventory id
        project_inv_query_set = ProjectInventory.objects.raw('SELECT * FROM project_inventory')
        inventory_match = Inventory.objects.get(inventory_name=inventory_name_delete)

        for inventoryItem in project_inv_query_set:
            # Get match for inventory name to inventory id and item in correct project
            if((inventoryItem.project_id == project_id_int) and (inventoryItem.inventory == inventory_match)):
                # Perform check that quantity doesn't already equal 0, else decrease quantity of object in project_inv_query_set until 0
                if (inventoryItem.quantity == 0):
                    # Do nothing; nothing should change
                    print("This won't work, silly goose!")
                else:
                    inventoryItem.quantity -= quantity_amount_delete_int
                    if (inventoryItem.quantity < 0):
                        # Prevent under 0 errors
                        inventoryItem.quantity = 0
                    # Now, need to update DB with this info
                    cursor.execute("""UPDATE project_inventory 
                                      SET quantity = %s
                                      WHERE project_id = %s
                                      AND inventory_id = %s
                                      """, [inventoryItem.quantity, project_id_int, inventory_match.inventory_id])
    # Standard inventory display
    cursor.execute("""SELECT inventory_name, inventory_description, quantity
                      FROM project_inventory, inventory
                      WHERE project_inventory.project_id = %s
                      AND project_inventory.inventory_id = inventory.inventory_id;
                   """, [project_id_int])

    query_set_append = cursor.fetchall()
    cursor.close()
    return render(request, 'DB3450Repo/projectInventory.html', {'projInventory': query_set_append})

# Retrieve information for purchases belonging specifically to a given project
def projectPurchases_view(request):
    project_id_int = request.session.get('project_id')
    cursor = connection.cursor()
    cursor.execute("""SELECT INVENTORY_NAME, PURCHASE_QUANTITY, PURCHASE_TOTAL, PURCHASE_DATE
                       FROM purchase, inventory
                       WHERE purchase.PROJECT_ID = %s
                       AND purchase.INVENTORY_ID = inventory.INVENTORY_ID;
                    """, [project_id_int])
    query_set_append = cursor.fetchall()
    cursor.close()

    return render(request, 'DB3450Repo/projectPurchases.html', {'projPurchases': query_set_append})


# CUSTOMER LINK HANDLING
def customerContactAdd_view(request):
    if request.GET.get('customer_contact_add_id'):
        customer_contact_id = request.GET('customer_contact_add_id')
        cus_con_add_id_int = int(customer_contact_id)
        customer_id = request.GET('customer_add_id')
        cus_id_int = int(customer_id)
        customer_contact_fname = request.GET('customer_contact_add_fname')
        customer_contact_lname = request.GET('customer_contact_add_lname')
        customer_contact_email = request.GET('customer_contact_add_email')
        customer_contact_tel = request.GET('customer_contact_add_tel')
        customer_contact_role = request.GET('customer_contact_add_role')
        customer_contact_current = request.GET('customer_contact_add_current')
        cursor = connection.cursor()
        cursor.execute("INSERT INTO customer_contact VALUES(%s,%s,%s,%s,%s,%s,%s,%s)", [
                       cus_con_add_id_int, cus_id_int, customer_contact_fname, customer_contact_lname, customer_contact_email, customer_contact_tel, customer_contact_role, customer_contact_current])
        connection.commit()
        cursor.close()

    return render(request, 'DB3450Repo/customerContactAdd.html')

def customerContactUpdate_view(request):
    if request.GET.get('customer_contact_add_id'):
        customer_contact_id = request.GET('customer_contact_add_id')
        customer_contact_id_int = int(customer_contact_id)
        customer_id = request.GET('customer_add_id')
        customer_id_int = int(customer_id)
        customer_contact_fname = request.GET('customer_contact_add_fname')
        customer_contact_lname = request.GET('customer_contact_add_lname')
        customer_contact_email = request.GET('customer_contact_add_email')
        customer_contact_tel = request.GET('customer_contact_add_tel')
        customer_contact_role = request.GET('customer_contact_add_role')
        customer_contact_current = request.GET('customer_contact_add_current')
        cursor = connection.cursor()
        cursor.execute("UPDATE customer_contact SET customer_contact_id = %s,customer_id = %s, customer_contact_fname = %s, customer_contact_email = %s,customer_contact_lname = %s,customer_contact_tel = %s, customer_contact_role = %s, customer_contact_current = %s WHERE customer_contact_id = %s AND customer_id = %s ", [
                       customer_contact_id_int, customer_id_int, customer_contact_fname, customer_contact_lname, customer_company_email, customer_contact_tel, customer_contact_role, customer_contact_current, customer_contact_id_int, customer_id_int])
        connection.commit()
        cursor.close()

    context = {
        'object_instance': query_set,
    }
    return render(request, 'DB3450Repo/supplierContactAfterUpdate.html', context)

def supplierContactAdd_view(request):
    query_set = SupplierContact.objects.raw('SELECT * FROM supplier_contact')
    supplier_query_set_append = []

    for obj in query_set:
        supplier_query_set_append.append(obj.supplier_contact_supplier)

    context = {
        'object_instance': query_set,
        'supplier_object_instance': supplier_query_set_append
    }
    return render(request, 'DB3450Repo/supplierContactAdd.html', context)

def supplierContactAfterAdd_view(request):
    supplier_name_req = request.GET['supplier_name']
    fname_req = request.GET['supplier_contact_fname']
    lname_req = request.GET['supplier_contact_lname']
    email_req = request.GET['supplier_contact_email']
    tel_req = request.GET['supplier_contact_tel']
    role_req = request.GET['supplier_contact_role']
    current_req = request.GET['supplier_contact_current']
    id_req_int = 0

    current_req_int = int(current_req)

    supplier_query_set = SupplierCompany.objects.raw('SELECT * FROM supplier_company')

    newSupplier = SupplierCompany.objects.get(supplier_company_name = supplier_name_req)

    # newValidSupplier = SupplierContact(
    #     supplier_contact_supplier = newSupplier,
    #     supplier_contact_fname = fname_req,
    #     supplier_contact_lname = lname_req,
    #     supplier_contact_email = email_req,
    #     supplier_contact_tel = tel_req,
    #     supplier_contact_role = role_req,
    #     supplier_contact_current = current_req_int 
    #     )

    # newValidSupplier.save()

    cursor = connection.cursor()
    cursor.execute('INSERT INTO supplier_contact (supplier_contact_supplier_id, supplier_contact_fname, supplier_contact_lname, supplier_contact_email, supplier_contact_tel, supplier_contact_role, supplier_contact_current) VALUES (%s,%s,%s,%s,%s,%s,%s)', [newSupplier.supplier_company_id, fname_req, lname_req, email_req, tel_req, role_req, current_req_int])
    connection.commit()

    query_set = SupplierContact.objects.raw('SELECT * FROM supplier_contact')
    supplier_query_set_append = []

    for obj in query_set:
        supplier_query_set_append.append(obj.supplier_contact_supplier)

    context = {
        'object_instance': query_set,
        'supplier_object_instance': supplier_query_set_append
    }

    return render(request, 'DB3450Repo/supplierContactAfterAdd.html', context)

# CUSTOMER LINK HANDLING ----------------------------------------------------------------------------------------------

def customerLanding_view(request):
    return render(request, 'DB3450Repo/customerLanding.html')

def customerContactAdd_view(request):
    if request.GET.get('Customer_add_id'):
        customer_id = request.GET['Customer_add_id']
        cus_id_int = int(customer_id)
        customer_contact_fname = request.GET['Customer_contact_add_fname']
        customer_contact_lname = request.GET['Customer_contact_add_lname']
        customer_contact_email = request.GET['Customer_contact_add_email']
        customer_contact_tel = request.GET['Customer_contact_add_tel']
        customer_contact_role = request.GET['Customer_contact_add_role']
        customer_contact_current = request.GET['Customer_contact_add_current']
        customer_contact_cur_int = int(customer_contact_current)
        cursor = connection.cursor()
        cursor.execute("INSERT INTO customer_contact(CUSTOMER_ID, CUSTOMER_CONTACT_FNAME, CUSTOMER_CONTACT_LNAME, CUSTOMER_CONTACT_EMAIL, CUSTOMER_CONTACT_TEL, CUSTOMER_CONTACT_ROLE, CUSTOMER_CONTACT_CURRENT) VALUES(%s,%s,%s,%s,%s,%s,%s)", [
                        cus_id_int, customer_contact_fname, customer_contact_lname, customer_contact_email, customer_contact_tel, customer_contact_role, customer_contact_cur_int])
        connection.commit()
        cursor.close()

    return render(request, 'DB3450Repo/customerContactAdd.html')

def customerContactUpdate_view(request):
    if request.GET.get('customer_contact_add_id'):
        customer_contact_id = request.GET['customer_contact_add_id']
        customer_contact_id_int = int(customer_contact_id)
        customer_id = request.GET['customer_add_id']
        customer_id_int = int(customer_id)
        customer_contact_fname = request.GET['customer_contact_add_fname']
        customer_contact_lname = request.GET['customer_contact_add_lname']
        customer_contact_email = request.GET['customer_contact_add_email']
        customer_contact_tel = request.GET['customer_contact_add_tel']
        customer_contact_role = request.GET['customer_contact_add_role']
        customer_contact_current = request.GET['customer_contact_add_current']
        cus_con_cur_int = int(customer_contact_current)
        cursor = connection.cursor()
        cursor.execute("UPDATE customer_contact SET customer_contact_id = %s,customer_id = %s, customer_contact_fname = %s, customer_contact_lname = %s,customer_contact_email = %s,customer_contact_tel = %s, customer_contact_role = %s, customer_contact_current = %s WHERE customer_contact_id = %s AND customer_id = %s ", [
                       customer_contact_id_int, customer_id_int, customer_contact_fname, customer_contact_lname, customer_contact_email, customer_contact_tel, customer_contact_role, cus_con_cur_int, customer_contact_id_int, customer_id_int])
        connection.commit()
        cursor.close()

    return render(request, 'DB3450Repo/customerContactUpdate.html')

def customerCompanyUpdate_view(request):
    if request.GET.get('customer_company_add_id'):
        customer_company_id_request = request.GET['customer_company_add_id']
        customer_company_id_int_request = int(customer_company_id_request)
        customer_company_name_request = request.GET['customer_company_add_name']
        customer_company_street1_request = request.GET['customer_company_add_street1']
        customer_company_street2_request = request.GET['customer_company_add_street2']
        customer_company_city_request = request.GET['customer_company_add_city']
        customer_company_state_request = request.GET['customer_company_add_state']
        customer_company_zip_request = request.GET['customer_company_zip']
        employee_id_r = request.GET['employee_add_id']
        employee_id_int_request = int(employee_id_r)
        cursor = connection.cursor()
        cursor = connection.cursor("UPDATE customer_company SET customer_company_id = %s, customer_company_name = %s, customer_company_street1 = %s, customer_company_street2 = %s, customer_company_city = %s, customer_company_state = %s, customer_company_zip = %s, employee_id = %s ", [
                                    customer_company_id_int_request, customer_company_name_request, customer_company_street1_request, customer_company_street2_request, customer_company_city_request, customer_company_state_request, customer_company_zip_request, employee_id_int_request])
        cursor.execute()
        connection.commit()
        cursor.close()

    return render(request, 'DB3450Repo/customerCompanyUpdate.html')


def customerCompanyAdd_view(request):
    if request.GET.get('customer_company_add_name'):
        customer_company_name_request = request.GET['customer_company_add_name']
        customer_company_street1_request = request.GET['customer_company_add_street1']
        customer_company_street2_request = request.GET['customer_company_add_street2']
        customer_company_city_request = request.GET['customer_company_add_city']
        customer_company_state_request = request.GET['customer_company_add_state']
        customer_company_zip_request = request.GET['customer_company_add_zip']
        customer_company_zip_int = int(customer_company_zip_request)
        employee_id_r = request.GET['employee_add_id']
        employee_id_int_request = int(employee_id_r)
        cursor = connection.cursor()
        cursor.execute("INSERT INTO customer_company(CUSTOMER_COMPANY_NAME, CUSTOMER_COMPANY_STREET1, CUSTOMER_COMPANY_STREET2, CUSTOMER_COMPANY_CITY, CUSTOMER_COMPANY_STATE, CUSTOMER_COMPANY_ZIP, EMPLOYEE_ID) VALUES(%s,%s,%s,%s,%s,%s,%s)", [
                        customer_company_name_request, customer_company_street1_request, customer_company_street2_request, customer_company_city_request, customer_company_state_request, customer_company_zip_int, employee_id_int_request])
        connection.commit()
        cursor.close()

    return render(request, 'DB3450Repo/customerCompanyAdd.html')


