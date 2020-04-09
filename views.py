from django.shortcuts import render
from django.http import HttpResponse
from construction_company.models import Inventory
    

def index(request):
    return render(request, 'construction_company/home.html')

def inventory_view(request):
    query_set = Inventory.objects.raw('SELECT * FROM Inventory')
    context = {
        'object_instance' : query_set
    }
    return render(request, 'construction_company/inventory.html', context)

def inventoryQuery_view(request):
    return render(request, 'construction_company/inventoryQuery.html')

def inventoryDetails_view(request):
    inventory_name = request.GET['inventory_name']
    inventory_description = request.GET['inventory_description']
    query_set_append = []
    query_set = Inventory.objects.raw('SELECT * FROM Inventory')
    for object in query_set:
            if(inventory_name == object.inventory_name):
                query_set_append.append(object)


    context = {
        'object_instance' : query_set_append
    }

    return render(request, 'construction_company/inventoryDetails.html', context)



