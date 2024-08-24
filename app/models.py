from django.db import models
from django.contrib.auth.models import User

CATEGORY = {
    ('Stationary', 'Stationary'),
    ('Food', 'Food'),
}
# Create your models here.




class Product(models.Model):
    name=models.CharField(max_length=250)
    category=models.CharField(max_length=10)
    quantity=models.PositiveIntegerField(null=True)
    description = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    created = models.CharField(max_length=50)
    o_quantity = models.PositiveIntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product} ordered quantity {self.o_quantity}"