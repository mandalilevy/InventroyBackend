from django.db import models

# Create your models here.
class InventoryRegistration(models.Model):
    itemID=models.CharField(max_length=255)
    itemName=models.CharField(max_length=255)
    itemQuantity=models.IntegerField()
