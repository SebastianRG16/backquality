from django.contrib import admin
from .models.branch_office import BranchOffice
from .models.cost_center import CostCenter
# Register your models here.
admin.site.register(BranchOffice)
admin.site.register(CostCenter)