from rest_framework import mixins, viewsets

from products.models import Product
from api.serializers import ProductSerializer


class CreateListViewSet(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    pass


class ProductViewSet(CreateListViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
