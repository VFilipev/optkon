from django.db import models
from catalog.models import Product
# from django.contrib.sessions.models import Session

# Create your models here.

class Order(models.Model):
    # session = models.ForeignKey(Session,blank=True,null=True,on_delete=models.SET_NULL)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True,null=True)
    STATUS_CHOICE = (
    ('N','Новый'),
    ('A','Подтвержден'),
    ('S','Оплачен'),
    ('D','Отменен'),
    )
    status = models.CharField(choices=STATUS_CHOICE,max_length=2,default="N")
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.PROTECT)
    product = models.ForeignKey(Product,blank=True,null=True,on_delete=models.CASCADE)
    count = models.IntegerField()
