from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import ProductViewSet

v1_router = DefaultRouter()
v1_router.register('products', ProductViewSet, basename='products')

urlpatterns = [
    path('v1/', include(v1_router.urls)),
]
