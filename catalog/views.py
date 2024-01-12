from rest_framework import viewsets
from django_filters import FilterSet
from catalog.models import Product
from django_filters.rest_framework import DjangoFilterBackend
from . serializers import ProductSerializer

class LodgeSetFilter(FilterSet):
    class Meta:
        model = Product
        fields = ['name', 'available']

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    model = Product
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend,]
    filterset_class  = LodgeSetFilter
