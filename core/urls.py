from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CompanyListCreateView, 
    EntityCatalogListCreateView,
)

#Rutas para Company
router = DefaultRouter()
router.register(r'companies', CompanyListCreateView, basename='companies')
#Rutas para EntityCatalog
router.register(r'entity-catalogs', EntityCatalogListCreateView, basename='entity-catalogs')

urlpatterns = [
    path('', include(router.urls)),
]
