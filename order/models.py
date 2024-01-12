from django.db import models
from catalog.models import Product
# from django.contrib.sessions.models import Session
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import send_mail

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
    def send_mail(self):
        msg = render_to_string('order_mail.html', {'order':self})
        send_mail('[Заказ] %d' %self.id , msg, settings.EMAIL_HOST_USER, [settings.ADMIN_EMAIL], html_message=msg)

class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.PROTECT)
    product = models.ForeignKey(Product,on_delete=models.PROTECT)
    count = models.IntegerField()
