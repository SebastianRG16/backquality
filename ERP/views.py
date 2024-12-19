from rest_framework import viewsets
from .models.branch_office import BranchOffice
from .models.cost_center import CostCenter
from .serializer import BranchOfficeSerializer, CostCenterSerializer
from .utils import get_accessible_data

class BranchOfficeViewSet(viewsets.ModelViewSet):
    """
    API para gestionar las Sucursales de una Compañía.
    """
    serializer_class = BranchOfficeSerializer

    def get_queryset(self):
        user = self.request.user
        accessible_data = get_accessible_data(user.id_user)

        if not accessible_data or not isinstance(accessible_data, list):
            return BranchOffice.objects.none()

        branch_office_ids = [
            row['branch_office_id'] for row in accessible_data 
            if isinstance(row, dict) and 'branch_office_id' in row
        ]

        print(f"Branch Office IDs: {branch_office_ids}")

        if branch_office_ids:
            return BranchOffice.objects.filter(id_broff__in=branch_office_ids)

        return BranchOffice.objects.none()



class CostCenterViewSet(viewsets.ModelViewSet):
    """
    API para gestionar los Centros de Costo.
    """
    serializer_class = CostCenterSerializer

    def get_queryset(self):
        user = self.request.user
        accessible_data = get_accessible_data(user.id_user)

        print(f"Accessible Data: {accessible_data}")

        if not accessible_data or not isinstance(accessible_data, list):
            return CostCenter.objects.none()

        cost_center_ids = [
            row['cost_center_id'] for row in accessible_data 
            if isinstance(row, dict) and 'cost_center_id' in row
        ]

        print(f"Cost Center IDs: {cost_center_ids}")

        if cost_center_ids:
            return CostCenter.objects.filter(id_cosce__in=cost_center_ids)

        return CostCenter.objects.none()


