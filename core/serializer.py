from rest_framework import serializers
from .models import Company, EntityCatalog

#Serializer para el modelo Company
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

#Serializer para el modelo EntityCatalog
class EntityCatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntityCatalog
        fields = '__all__'
