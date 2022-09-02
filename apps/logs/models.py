from django.db import models
from apps.users.models import User


class ActionType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Nombre', max_length=50, blank=True)
    creationDate = models.DateTimeField('Fecha de creación', auto_now_add=True)

    class Meta():
        db_table = 'action_types'

class Log(models.Model):
    id = models.AutoField(primary_key=True)
    users= models.ForeignKey(User, on_delete=models.PROTECT)
    actionType = models.ForeignKey(ActionType, on_delete=models.PROTECT)
    targetId = models.IntegerField('Id del objeto',blank=True, null=True)
    url = models.CharField('Url', max_length=500, blank=False,null=False)
    ipUser = models.CharField('IP de usuario', max_length=70, blank=False)
    value = models.CharField('Valor', max_length=70, blank=False)
    creationDate = models.DateTimeField('Fecha de creación', auto_now_add=True)


    class Meta():
        db_table = 'logs'