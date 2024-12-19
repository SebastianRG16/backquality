from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from user.models.user import User
from user.models.role import Role
from user.models.permi_role import PermiRole
from user.models.permi_role_record import PermiRoleRecord
from user.models.permi_user import PermiUser
from user.models.permi_user_record import PermiUserRecord
from user.models.permission import Permission
from user.models.user_company import UserCompany
from .serializer import LoginSerializer,UserSerializer, RoleSerializer, UserCompanySerializer, PermiRoleSerializer, PermissionSerializer, PermiUserSerializer, PermiUserRecordSerializer, PermiRole, PermiRoleRecordSerializer


class LoginView(APIView):
    """
    Vista para manejar el login y generar los tokens JWT.
    """
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            return Response({
                'refresh': str(refresh),
                'access': access_token,
                'user': {
                    'id_user': user.id_user,
                    'user_username': user.user_username,
                    'user_email': user.user_email,
                    'user_phone': user.user_phone,
                    'user_is_admin': user.user_is_admin,
                    'user_is_active': user.user_is_active,
                    'roles': [role.role_name for role in user.roles.all()],
                    'permissions': [permission.name for permission in user.permissions.all()]
                }
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Vista para User
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Vista para UserCompany
class UserCompanyViewSet(viewsets.ModelViewSet):
    queryset = UserCompany.objects.all()
    serializer_class = UserCompanySerializer

# Vista para Role
class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

# Vista para Permission
class PermissionViewSet(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer

# Vista para PermiUser
class PermiUserViewSet(viewsets.ModelViewSet):
    queryset = PermiUser.objects.all()
    serializer_class = PermiUserSerializer

# Vista para PermiUserRecord
class PermiUserRecordViewSet(viewsets.ModelViewSet):
    queryset = PermiUserRecord.objects.all()
    serializer_class = PermiUserRecordSerializer

# Vista para PermiRole
class PermiRoleViewSet(viewsets.ModelViewSet):
    queryset = PermiRole.objects.all()
    serializer_class = PermiRoleSerializer

# Vista para PermiRoleRecord
class PermiRoleRecordViewSet(viewsets.ModelViewSet):
    queryset = PermiRoleRecord.objects.all()
    serializer_class = PermiRoleRecordSerializer