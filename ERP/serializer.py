from rest_framework import serializers
from .models.branch_office import BranchOffice
from .models.cost_center import CostCenter

#Serializer para el modelo branch_office
class BranchOfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BranchOffice
        fields = '__all__'
        extra_kwargs = {
            'broff_name': {'required': True},
            'broff_code': {'required': True}
        }

#Serializer para el modelo cost_center
class CostCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CostCenter
        fields = '__all__'
        extra_kwargs = {
            'cosce_code': {'required': True},
            'cosce_name': {'required': True}
        }
