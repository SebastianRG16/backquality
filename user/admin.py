from django.contrib import admin
from .models.user import User
from .models.user_company import UserCompany
from .models.role import Role
from .models.permission import Permission
from .models.permi_user import PermiUser
from .models.permi_user_record import PermiUserRecord
from .models.permi_role import PermiRole
from .models.permi_role_record import PermiRoleRecord

# Register your models here.
admin.site.register(User)
admin.site.register(UserCompany)
admin.site.register(Role)
admin.site.register(Permission)
admin.site.register(PermiUser)
admin.site.register(PermiUserRecord)
admin.site.register(PermiRole)
admin.site.register(PermiRoleRecord)