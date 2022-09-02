from django.db import models


class Book(models.Model):

    id = models.AutoField(primary_key=True)
    title= models.CharField('Titulo', max_length=100, blank=False,null=False)
    author = models.CharField('Autor', max_length=100, blank=False,null=False)
    editorial = models.CharField('Editorial', max_length=100, blank=False,null=False)
    createdDate = models.DateTimeField('Fecha de creación', auto_now_add=True)
    modifiedDate = models.DateTimeField('Fecha de modifiación', auto_now=True) 


    class Meta():
        db_table = 'books'