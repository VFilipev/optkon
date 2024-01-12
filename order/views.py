from rest_framework import viewsets
from django_filters import FilterSet
from order.models import Order
from django_filters.rest_framework import DjangoFilterBackend
from . serializers import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    model = Order
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend,]