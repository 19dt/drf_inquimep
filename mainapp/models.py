from django.db import models
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.forms import model_to_dict



# Create your models here.
class Meta:
    model = User
    fields = ['username','email','first_name', 'last_name','password1', 'password2', 'is_staff']

# Model client
class Client(models.Model):
    nif = models.CharField(max_length= 9, null = False, verbose_name='NIF', unique=True)
    business_name = models.CharField(max_length=200, null = False, verbose_name='Nombre de la Empresa', unique=True)
    country = models.CharField(max_length=50,null = False, verbose_name='Pais')
    province = models.CharField(max_length=200, null = False, verbose_name='Provincia')
    town = models.CharField(max_length=200,null = False, verbose_name='Ciudad')
    postal_code = models.CharField(max_length=100, null = False, verbose_name='Código postal')
    phone = models.IntegerField(null = False, verbose_name='Teléfono')
    email = models.EmailField(max_length=100, null = False, verbose_name='Email')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.business_name
    
    def toJSON(self):
        item = model_to_dict(self)
        return item


    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['id']

class Entry(models.Model):
    number = models.IntegerField(null= False, verbose_name = 'Número')
    lot = models.IntegerField(null=False, verbose_name = 'Lote')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=False, verbose_name='Cliente')
    type = models.CharField(max_length=200, null=False, verbose_name='Tipo')
    reference = models.CharField(max_length=200, null=False, verbose_name='Referencia')
    reception_weight = models.DecimalField(max_digits=5, decimal_places=2,null=False, verbose_name='Peso recepción')
    starting_weight = models.DecimalField(max_digits=5, decimal_places=2,null= False, verbose_name='Peso inicial')
    w_b_d= models.DecimalField(max_digits=5, decimal_places=2,null=False, verbose_name= 'Peso antes de taladro')
    w_a_d = models.DecimalField(max_digits=5, decimal_places=2,null =False, verbose_name='Peso después de taladro')
    observations = models.TextField(null= True, verbose_name= 'Observaciones')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.number} ({self.client.business_name})'

    def toJSON(self):
        item = model_to_dict(self)
        item['client'] = self.client.toJSON()
        return item

    class Meta:
        db_table = 'entry'
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'
        ordering = ['id']
        
