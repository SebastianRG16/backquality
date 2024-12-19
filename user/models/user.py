from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

class UserManager(BaseUserManager):
    def create_user(self, user_username, user_email, user_password=None, **extra_fields):
        """
        Crea y devuelve un usuario con un correo electrónico y una contraseña.
        """
        if not user_email:
            raise ValueError(_('El correo electrónico es obligatorio'))
        email = self.normalize_email(user_email)
        user = self.model(user_username=user_username, user_email=email, **extra_fields)
        user.set_password(user_password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_username, user_email, password=None, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        # Usar los campos correctos para el modelo User
        return self.create_user(user_username, user_email, password, **extra_fields)



class User(AbstractBaseUser, PermissionsMixin):
    """
    Modelo de Usuario personalizado
    """
    id_user = models.BigAutoField(
        primary_key=True,
        verbose_name="ID de Usuario",
        help_text="Identificador único para el usuario."
    )

    user_username = models.CharField(
        unique=True,
        verbose_name=_("Nombre de Usuario"),
        help_text=_("Nombre de usuario para iniciar sesión.")
    )

    user_password = models.CharField(
        verbose_name=_("Contraseña"),
        help_text=_("Contraseña encriptada del usuario.")
    )

    user_email = models.EmailField(
        unique=True,
        verbose_name=_("Correo Electrónico"),
        help_text=_("Dirección de correo electrónico del usuario.")
    )

    user_phone = models.CharField(
        blank=True,
        verbose_name=_("Teléfono"),
        help_text=_("Número de teléfono del usuario.")
    )

    user_is_admin = models.BooleanField(
        default=False,
        verbose_name=_("Usuario Administrador"),
        help_text=_("Indica si el usuario es Administrador (True) o normal (False).")
    )

    user_is_active = models.BooleanField(
        default=True,
        verbose_name=_("Usuario Activo"),
        help_text=_("Indica si el usuario está activo (True) o inactivo (False).")
    )

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # Relaciones con roles
    roles = models.ManyToManyField(
        'Role',
        related_name='users',
        verbose_name=_("Roles del Usuario"),
        help_text=_("Roles asignados al usuario.")
    )

    # Relaciones con permisos
    permissions = models.ManyToManyField(
        'Permission',
        related_name='users',
        verbose_name=_("Permisos del Usuario"),
        help_text=_("Permisos específicos asignados al usuario."),
        blank=True
    )

    objects = UserManager()

    USERNAME_FIELD = 'user_username'
    REQUIRED_FIELDS = ['user_email']

    class Meta:
        verbose_name = _("Usuario")
        verbose_name_plural = _("Usuarios")

    def get_user_id(self):
        return self.id_user

    def __str__(self):
        return self.user_username
