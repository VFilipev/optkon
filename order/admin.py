from django.contrib import admin
from order.models import Order,OrderItem

class InlineOrderItemAdmin(admin.TabularInline):
    model = OrderItem


# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','name','phone','email']
    inlines=[
        InlineOrderItemAdmin
    ]
    pass


