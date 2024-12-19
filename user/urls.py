from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import LoginView

router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename='user')
router.register(r'user_companies', views.UserCompanyViewSet, basename='user_company')
router.register(r'roles', views.RoleViewSet, basename='role')
router.register(r'permissions', views.PermissionViewSet, basename='permission')
router.register(r'permi_users', views.PermiUserViewSet, basename='permi_user')
router.register(r'permi_user_records', views.PermiUserRecordViewSet, basename='permi_user_record')
router.register(r'permi_roles', views.PermiRoleViewSet, basename='permi_role')
router.register(r'permi_role_records', views.PermiRoleRecordViewSet, basename='permi_role_record')

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('', include(router.urls)),
]
