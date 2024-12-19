from django.contrib import admin
from .models.company import Company
from .models.entity_catalog import EntityCatalog
# Register your models here.
admin.site.register(Company)
admin.site.register(EntityCatalog)