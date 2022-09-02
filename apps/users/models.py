from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    class UserType(models.IntegerChoices):
        basic = 1
        admin = 2

    class Status(models.IntegerChoices):
        enabled = 1
        disabled = 2

    class DocumentType(models.IntegerChoices):
        cedula = 1
        tarjetaIdentidad = 2
        cedulaExtranjeria = 3
        pasaporte = 4

    id = models.AutoField(primary_key=True)
    first_name = models.CharField('Nombres', max_length=70, blank=False, null=False)
    last_name = models.CharField('Apellidos',max_length=70, blank=False, null=False)
    documentType = models.IntegerField('Tipo de documento',choices=DocumentType.choices, default=1)
    document = models.CharField('Identificación', max_length=50, blank=False, null=False, unique=True)
    email = models.EmailField('Correo electrónico', max_length=50, blank=False, null=False, unique=True)
    password = models.CharField('Contraseña', max_length=100, blank=False, null=False)
    username = models.CharField('Nombre de usuario', max_length=70, blank=False, null=False, unique=True)
    cellphone = models.CharField('Número de contacto', max_length=15,blank=False, null=False) 
    userType = models.IntegerField('Tipo de usuario', choices=UserType.choices,default=1)
    status = models.IntegerField('Estado', choices=Status.choices,default=1)
    createdDate = models.DateTimeField('Fecha de creación', auto_now_add=True)
    modifiedDate = models.DateTimeField('Fecha de modifiación', auto_now=True)

    class Meta:
        db_table = 'users'

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']