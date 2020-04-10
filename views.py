from django.shortcuts import render
from django.http import HttpResponse
from construction_company.models import Inventory
from construction_company.models import EmployeePermission
from construction_company.models import Employee
from construction_company.models import Permission
from construction_company.models import Project
from datetime import date
    

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



