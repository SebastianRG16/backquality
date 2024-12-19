from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    BranchOfficeViewSet,
    CostCenterViewSet,
)

router = DefaultRouter()
#Rutas para Sucursales
router.register(r'branch', BranchOfficeViewSet, basename='branch')
#Rutas para Costo
router.register(r'cost', CostCenterViewSet, basename='cost')

urlpatterns = [
    path('', include(router.urls)),
]
