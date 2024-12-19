from rest_framework import viewsets
from .models.company import Company
from .models.entity_catalog import EntityCatalog
from .serializer import CompanySerializer, EntityCatalogSerializer

#Views para el modelo Company
class CompanyListCreateView(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer



#Views para el modelo EntityCatalog
class EntityCatalogListCreateView(viewsets.ModelViewSet):
    queryset = EntityCatalog.objects.all()
    serializer_class = EntityCatalogSerializer

