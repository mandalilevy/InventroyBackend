from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from inventory.serializers import InventorySerializer
from inventory.models import InventoryRegistration

@csrf_exempt
def InventoryAPI(request, id=0):
    if request.method=='GET':
        item=InventoryRegistration.objects.all()
        item_serializer=InventorySerializer(item,many=True)
        return JsonResponse(item_serializer.data,safe=False)
    elif request.method=='POST':
        item=JSONParser().parse(request)
        item_serializer=InventorySerializer(data=item)
        if item_serializer.is_valid():
            item_serializer.save()
            return JsonResponse("New item saved",safe=False)
        return JsonResponse("Failed to add Item",safe=False)
    
    elif request.method=='PUT':
        item=JSONParser().parse(request)
        itemID=InventoryRegistration.objects.get(id=id)
        item_serializer=InventorySerializer(itemID,data=item)
        if item_serializer.is_valid():
            item_serializer.save()
            return JsonResponse("Item Updated!",safe=False)
        return JsonResponse("Failed to update Item",safe=False)
    elif request.method=='DELETE':
        itemID=InventoryRegistration.objects.get(id=id)
        itemID.delete()
        return JsonResponse("Item Deleted!",safe=False)


