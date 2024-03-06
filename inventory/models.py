from django.db import models
from django.utils.translation import gettext_lazy as _
from categories.models import Category
from suppliers.models import Supplier
from employees.models import Employee

# Create your models here.

class Inventory(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    unit = models.CharField(max_length=20, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True)
    stock_quantity = models.IntegerField(default=0)
    reorder_point = models.IntegerField(default=0)
    minimum_stock = models.IntegerField(default=0)
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='inventory_images/', blank=True, null=True)

    class Meta:
        db_table = 'inventory'

class InventoryHistory(models.Model):
    ACTIONS = [
        ('ADD', 'Add'),
        ('SUBTRACT', 'Subtract'),
        ('TRANSFER', 'Transfer'),
    ]

    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    transaction_date = models.DateTimeField(auto_now_add=True)
    quantity_change = models.IntegerField()
    action = models.CharField(max_length=50, choices=ACTIONS)
    user = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    note = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'inventory_history'