from django.db import models
from mainapp.models import Client
from django.forms import model_to_dict

# Create your models here.
# Model analysis
class Analysis(models.Model):
    number = models.IntegerField(null= False, verbose_name = 'Número')
    lot = models.IntegerField(null=False, verbose_name = 'Lote')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=False, verbose_name='Cliente')
    type = models.CharField(max_length=200, null=False, verbose_name='Tipo')
    observations = models.TextField(null= True, verbose_name= 'Observaciones')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.client
    
    def toJSON(self):
        item = model_to_dict(self)
        item['client'] = self.client.toJSON()
        return item

    class Meta:
        abstract = True
        
class Gold(Analysis):
    witness = models.CharField(max_length=200, verbose_name = 'Testigo')
    sample_1_reception_weight = models.DecimalField(max_digits=5, decimal_places=2,blank = False, null = False, verbose_name = 'Muestra 1 - Peso Inicial')
    sample_1_final_weight = models.DecimalField(max_digits=5, decimal_places=2,null = False, verbose_name = 'Muestra 1 - Peso Final')
    sample_1_law = models.CharField(max_length=200, verbose_name='Muestra 1 - Ley') 
    sample_1_discard = models.BooleanField(verbose_name = 'Muestra 1 - Descartar')
    sample_2_reception_weight = models.DecimalField(max_digits=5, decimal_places=2,null = False, verbose_name = 'Muestra 2 - Peso Inicial')
    sample_2_final_weight = models.DecimalField(max_digits=5, decimal_places=2,null = False, verbose_name = 'Muestra 2 - Peso Final')
    sample_2_law = models.CharField(max_length=200, verbose_name='Muestra 2 - Ley') 
    sample_2_discard = models.BooleanField(verbose_name = 'Muestra 2 - Descartar')
    sample_3_reception_weight = models.DecimalField(max_digits=5, decimal_places=2,null = False, verbose_name = 'Muestra 3 - Peso Inicial')
    sample_3_final_weight = models.DecimalField(max_digits=5, decimal_places=2,null = False, verbose_name = 'Muestra 3 - Peso Final')
    sample_3_law = models.CharField(max_length=200, verbose_name='Muestra 3 - Ley') 
    sample_3_discard = models.BooleanField(verbose_name = 'Muestra 3 - Descartar')
    sample_4_reception_weight = models.DecimalField(max_digits=5, decimal_places=2,null = False, verbose_name = 'Muestra 4 - Peso Inicial')
    sample_4_final_weight = models.DecimalField(max_digits=5, decimal_places=2,null = False, verbose_name = 'Muestra 4 - Peso Final')
    sample_4_law = models.CharField(max_length=200, verbose_name='Muestra 4 - Ley') 
    sample_4_discard = models.BooleanField(verbose_name = 'Muestra 4 - Descartar')
    sample_5_reception_weight = models.DecimalField(max_digits=5, decimal_places=2,null = False, verbose_name = 'Muestra 5 - Peso Inicial')
    sample_5_final_weight = models.DecimalField(max_digits=5, decimal_places=2,null = False, verbose_name = 'Muestra 5 - Peso Final')
    sample_5_law = models.CharField(max_length=200, verbose_name='Muestra 5 - Ley') 
    sample_5_discard = models.BooleanField(verbose_name = 'Muestra 5 - Descartar')
    sample_6_reception_weight = models.DecimalField(max_digits=5, decimal_places=2,null = False, verbose_name = 'Muestra 6 - Peso Inicial')
    sample_6_final_weight = models.DecimalField(max_digits=5, decimal_places=2,null = False, verbose_name = 'Muestra 6 - Peso Final')
    sample_6_law = models.CharField(max_length=200, verbose_name='Muestra 6 - Ley') 
    sample_6_discard = models.BooleanField(verbose_name = 'Muestra 6 - Descartar')
    sample_7_reception_weight = models.DecimalField(max_digits=5, decimal_places=2,null = False, verbose_name = 'Muestra 7 - Peso Inicial')
    sample_7_final_weight = models.DecimalField(max_digits=5, decimal_places=2,null = False, verbose_name = 'Muestra 7 - Peso Final')
    sample_7_law = models.CharField(max_length=200, verbose_name='Muestra 7 - Ley') 
    sample_7_discard = models.BooleanField(verbose_name = 'Muestra 7 - Descartar')
    sample_8_reception_weight = models.DecimalField(max_digits=5, decimal_places=2,null = False, verbose_name = 'Muestra 8 - Peso Inicial')
    sample_8_final_weight = models.DecimalField(max_digits=5, decimal_places=2,null = False, verbose_name = 'Muestra 8 - Peso Final')
    sample_8_law = models.CharField(max_length=200, verbose_name='Muestra 8 - Ley') 
    sample_8_discard = models.BooleanField(verbose_name = 'Muestra 8 - Descartar')
    final_law = models.TextField(null=False, verbose_name = 'Ley final')
        
    def __str__(self):
        return self.witness

class Silver(Analysis):
    witness = models.CharField(max_length=200, null=False, verbose_name = 'Testigo')
    sample_1_weight = models.DecimalField(max_digits=5, decimal_places=2,null = False, verbose_name = 'Muestra 1 - Peso')
    sample_1_law = models.CharField(max_length=200, null = False, verbose_name = 'Muestra 1 - Ley')
    sample_1_discard = models.BooleanField(verbose_name = 'Muestra 1 - Descartar')
    sample_2_weight = models.DecimalField(max_digits=5, decimal_places=2,null = False, verbose_name = 'Muestra 2 - Peso')
    sample_2_law = models.CharField(max_length=200, null = False, verbose_name = 'Muestra 2 - Ley')
    sample_2_discard = models.BooleanField(verbose_name = 'Muestra 2 - Descartar')
    sample_3_weight = models.DecimalField(max_digits=5, decimal_places=2,null = False, verbose_name = 'Muestra 3 - Peso')
    sample_3_law = models.CharField(max_length=200, null = False, verbose_name = 'Muestra 3 - Ley')
    sample_3_discard = models.BooleanField(verbose_name = 'Muestra 3 - Descartar')
    sample_4_weight = models.DecimalField(max_digits=5, decimal_places=2,null = False, verbose_name = 'Muestra 4 - Peso')
    sample_4_law = models.CharField(max_length=200, null = False, verbose_name = 'Muestra 4 - Ley')
    sample_4_discard = models.BooleanField(verbose_name = 'Muestra 4 - Descartar')
    sample_5_weight = models.DecimalField(max_digits=5, decimal_places=2,null = False, verbose_name = 'Muestra 5 - Peso')
    sample_5_law = models.CharField(max_length=200, null = False, verbose_name = 'Muestra 5 - Ley')
    sample_5_discard = models.BooleanField(verbose_name = 'Muestra 5 - Descartar')
    sample_6_weight = models.DecimalField(max_digits=5, decimal_places=2,null = False, verbose_name = 'Muestra 6 - Peso')
    sample_6_law = models.CharField(max_length=200, null = False, verbose_name = 'Muestra 6 - Ley')
    sample_6_discard = models.BooleanField(verbose_name = 'Muestra 6 - Descartar')
    sample_7_weight = models.DecimalField(max_digits=5, decimal_places=2,null = False, verbose_name = 'Muestra 7 - Peso')
    sample_7_law = models.CharField(max_length=200, null = False, verbose_name = 'Muestra 7 - Ley')
    sample_7_discard = models.BooleanField(verbose_name = 'Muestra 7 - Descartar')
    sample_8_weight = models.DecimalField(max_digits=5, decimal_places=2,null = False, verbose_name = 'Muestra 8 - Peso')
    sample_8_law = models.CharField(max_length=200, null = False, verbose_name = 'Muestra 8 - Ley')
    sample_8_discard = models.BooleanField(verbose_name = 'Muestra 8 - Descartar')
    final_law = models.TextField(null=False, verbose_name = 'Ley Final', blank = False)

    def __str__(self):
        return self.witness
