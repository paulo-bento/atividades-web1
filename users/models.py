from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("O e-mail é obrigatório.")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    nome_completo = models.CharField(max_length=150)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["nome_completo"]

    def __str__(self):
        return self.email


class Documento(models.Model):
    CATEGORIAS = [
        ("identidade", "Identidade"),
        ("comprovante", "Comprovante de Residência"),
        ("outro", "Outro"),
    ]

    usuario = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="documentos"
    )
    arquivo = models.FileField(upload_to="uploads/")
    categoria = models.CharField(max_length=20, choices=CATEGORIAS, default="outro")
    data_envio = models.DateTimeField(auto_now_add=True)
    verificado = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.usuario.email} - {self.categoria}"
