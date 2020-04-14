from django.shortcuts import render
from django.http import HttpResponse
from DB3450Repo.models import Inventory
from DB3450Repo.models import InventorySupplier
from DB3450Repo.models import EmployeePermission
from DB3450Repo.models import Employee
from DB3450Repo.models import Permission
from DB3450Repo.models import Project
from DB3450Repo.models import EmployeeHours, SupplierCompany
from datetime import date
from django.db import connection
import django


def index(request):
    return render(request, 'DB3450Repo/home.html')


def inventory_view(request):
    query_set = Inventory.objects.raw('SELECT * FROM inventory')
    context = {
        'object_instance': query_set
    }
    return render(request, 'DB3450Repo/inventory.html', context)


def employeePermission_view(request):
    query_set = EmployeePermission.objects.raw(
        'SELECT * FROM employee_permission')
    employee_query_set = Employee.objects.raw('SELECT * FROM employee')
    permission_query_set = Permission.objects.raw('SELECT * FROM permission')
    employee_query_set_append = []
    permission_query_set_append = []

    for employeePermission in query_set:
        employee_query_set_append.append(employeePermission.employee)
        permission_query_set_append.append(employeePermission.permission_level)

    context = {
        'employee_object_instance': employee_query_set_append,
        'permission_object_instance': permission_query_set_append
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

    validEmployee = Employee.objects.get(employee_id=employee_id_request)

    for employeePermission in query_set:
        if(employeePermission.employee == validEmployee):
            employee_query_set_append.append(employeePermission.employee)
            permission_query_set_append.append(
                employeePermission.permission_level)

    context = {
        'employee_object_instance': employee_query_set_append,
        'permission_object_instance': permission_query_set_append
    }
    return render(request, 'DB3450Repo/employeePermissionDetails.html', context)


def employeePermissionAdd_view(request):
    query_set = EmployeePermission.objects.raw(
        'SELECT * FROM employee_permission')
    employee_query_set = Employee.objects.raw('SELECT * FROM employee')
    permission_query_set = Permission.objects.raw('SELECT * FROM permission')
    employee_query_set_append = []
    permission_query_set_append = []

    for employeePermission in query_set:
        employee_query_set_append.append(employeePermission.employee)
        permission_query_set_append.append(employeePermission.permission_level)

    context = {
        'employee_object_instance': employee_query_set_append,
        'permission_object_instance': permission_query_set_append
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

    context = {
        'employee_object_instance': employee_query_set_append,
        'permission_object_instance': permission_query_set_append
    }
    return render(request, 'DB3450Repo/employeePermission.html', context)


def employeePermissionDelete_view(request):
    query_set = EmployeePermission.objects.raw(
        'SELECT * FROM employee_permission')
    employee_query_set = Employee.objects.raw('SELECT * FROM employee')
    permission_query_set = Permission.objects.raw('SELECT * FROM permission')
    employee_query_set_append = []
    permission_query_set_append = []

    for employeePermission in query_set:
        employee_query_set_append.append(employeePermission.employee)
        permission_query_set_append.append(employeePermission.permission_level)

    context = {
        'employee_object_instance': employee_query_set_append,
        'permission_object_instance': permission_query_set_append
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


def inventoryAdd_view(request):
    query_set = Inventory.objects.raw('SELECT * FROM inventory')

    context = {
        'object_instance': query_set
    }
    return render(request, 'DB3450Repo/inventoryAdd.html', context)


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

    # query_set_append = []

    newInventory = Inventory.objects.get(inventory_id=inventory_id_request)
    newInventory.inventory_name = inventory_name_request
    newInventory.inventory_description = inventory_description_request
    newInventory.save()

    query_set = Inventory.objects.raw('SELECT * FROM inventory')
    context = {
        'object_instance': query_set
    }

    return render(request, 'DB3450Repo/inventoryAfterUpdate.html', context)


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

    newInventory = Inventory.objects.get(inventory_name=inventory_name_request)
    newSupplier = SupplierCompany.objects.get(
        supplier_company_name=supplier_company_request)

    validateInventory = InventorySupplier.objects.get(
        inventory_supplier_inventory=newInventory, supplier=newSupplier)

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


def supplierAddOrUpdate_view(request):
    query_set = SupplierCompany.objects.raw('SELECT * FROM supplier_company')

    context = {
        'object_instance': query_set,
    }
    return render(request, 'DB3450Repo/supplierAddOrUpdate.html', context)


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


def projectBudget_view(request):
    project_id_int = request.session.get('project_id')
    query_set_append = []
    query_set = Project.objects.raw('Select * FROM project')
    for object in query_set:
        if(project_id_int == object.project_id):
            query_set_append.append(object)

    context = {
        'budgetResults': query_set_append
    }

    return render(request, 'DB3450Repo/projectBudget.html', context)


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


def projectInventory_view(request):
    return render(request, 'DB3450Repo/projectInventory.html')


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
