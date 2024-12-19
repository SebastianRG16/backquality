from rest_framework import serializers
from user.models.permi_role import PermiRole
from user.models.permi_role_record import PermiRoleRecord
from user.models.permi_user import PermiUser
from user.models.permi_user_record import PermiUserRecord
from user.models.permission import Permission
from user.models.role import Role
from user.models.user import User
from django.contrib.auth import authenticate
from user.models.user_company import UserCompany
from core.models import Company, EntityCatalog
from rest_framework_simplejwt.tokens import RefreshToken


class LoginSerializer(serializers.Serializer):
    user_username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(user_username=data['user_username'], password=data['password'])
        if not user:
            raise serializers.ValidationError("Credenciales incorrectas")
        if not user.user_is_active:
            raise serializers.ValidationError("Usuario inactivo")
        return user

    def get_tokens(self, user):
        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['tokens'] = self.get_tokens(instance)
        user_data = UserSerializer(instance).data
        data['user'] = user_data
        
        return data

# Serializador de User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

# Serializador de UserCompany
class UserCompanySerializer(serializers.ModelSerializer):
    user = UserSerializer()
    company = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all())
    
    class Meta:
        model = UserCompany
        fields = '__all__'

# Serializador de Role
class RoleSerializer(serializers.ModelSerializer):
    company = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all())
    
    class Meta:
        model = Role
        fields = '__all__'

# Serializador de Permission
class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'

# Serializador de PermiUser
class PermiUserSerializer(serializers.ModelSerializer):
    usercompany = UserCompanySerializer()
    permission = PermissionSerializer()
    entitycatalog = serializers.PrimaryKeyRelatedField(queryset=EntityCatalog.objects.all())

    class Meta:
        model = PermiUser
        fields = '__all__'

# Serializador de PermiUserRecord
class PermiUserRecordSerializer(serializers.ModelSerializer):
    usercompany = UserCompanySerializer()
    permission = PermissionSerializer()
    entitycatalog = serializers.PrimaryKeyRelatedField(queryset=EntityCatalog.objects.all())
    
    class Meta:
        model = PermiUserRecord
        fields = '__all__'

# Serializador de PermiRole
class PermiRoleSerializer(serializers.ModelSerializer):
    role = serializers.PrimaryKeyRelatedField(queryset=Role.objects.all())
    permission = serializers.PrimaryKeyRelatedField(queryset=Permission.objects.all())
    entitycatalog = serializers.PrimaryKeyRelatedField(queryset=EntityCatalog.objects.all())
    
    class Meta:
        model = PermiRole
        fields = '__all__'

# Serializador de PermiRoleRecord
class PermiRoleRecordSerializer(serializers.ModelSerializer):
    role = RoleSerializer()
    permission = PermissionSerializer()
    entitycatalog = serializers.PrimaryKeyRelatedField(queryset=EntityCatalog.objects.all())
    
    class Meta:
        model = PermiRoleRecord
        fields = '__all__'
