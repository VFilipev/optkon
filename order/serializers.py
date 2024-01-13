from . models import Order, OrderItem
from rest_framework import serializers
from catalog.serializers import ProductSerializer
from order.models import OrderItem
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.db.models.signals import post_save
from django.dispatch import receiver

class ProductSetSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = OrderItem
        exclude = ('order',)

class OrderItemSerializer(serializers.ModelSerializer):
    products = ProductSerializer(read_only=True)
    class Meta:
        model = OrderItem
        fields = '__all__'
        depth = 1

class OrderSerializer(serializers.ModelSerializer):
    products_set = ProductSetSerializer(many=True, required=False)
    orderitem_set = OrderItemSerializer(many=True,read_only=True)
    class Meta:
        model = Order
        fields = '__all__'
        depth = 1

    def create(self, validated_data):
        orderitems_set = validated_data.pop('products_set')
        order = Order.objects.create(**validated_data)
        if orderitems_set:
            for orderitem in orderitems_set:
                if orderitem['product'] is not None:
                    OrderItem.objects.create(order = order, **orderitem)
        # order = {}
        #msg = render_to_string('order_mail.html', {'order':order})
        #send_mail('Заказ №%d' %order.id , msg, settings.EMAIL_HOST_USER, [settings.ADMIN_EMAIL], html_message=msg)
        return order
    
@receiver(post_save, sender=Order, dispatch_uid="send_mail")
def s_mail(sender, instance, **kwargs):
    msg = render_to_string('order_mail.html', {'order':instance})
    send_mail('Заказ №%d' %instance.id , msg, settings.EMAIL_HOST_USER, [settings.ADMIN_EMAIL], html_message=msg)    