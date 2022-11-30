# Generated by Django 4.1.3 on 2022-11-30 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Silver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(verbose_name='Número')),
                ('lot', models.IntegerField(verbose_name='Lote')),
                ('type', models.CharField(max_length=200, verbose_name='Tipo')),
                ('observations', models.TextField(null=True, verbose_name='Observaciones')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(auto_now_add=True)),
                ('witness', models.CharField(max_length=200, verbose_name='Testigo')),
                ('sample_1_weight', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Muestra 1 - Peso')),
                ('sample_1_law', models.CharField(max_length=200, verbose_name='Muestra 1 - Ley')),
                ('sample_1_discard', models.BooleanField(verbose_name='Muestra 1 - Descartar')),
                ('sample_2_weight', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Muestra 2 - Peso')),
                ('sample_2_law', models.CharField(max_length=200, verbose_name='Muestra 2 - Ley')),
                ('sample_2_discard', models.BooleanField(verbose_name='Muestra 2 - Descartar')),
                ('sample_3_weight', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Muestra 3 - Peso')),
                ('sample_3_law', models.CharField(max_length=200, verbose_name='Muestra 3 - Ley')),
                ('sample_3_discard', models.BooleanField(verbose_name='Muestra 3 - Descartar')),
                ('sample_4_weight', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Muestra 4 - Peso')),
                ('sample_4_law', models.CharField(max_length=200, verbose_name='Muestra 4 - Ley')),
                ('sample_4_discard', models.BooleanField(verbose_name='Muestra 4 - Descartar')),
                ('sample_5_weight', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Muestra 5 - Peso')),
                ('sample_5_law', models.CharField(max_length=200, verbose_name='Muestra 5 - Ley')),
                ('sample_5_discard', models.BooleanField(verbose_name='Muestra 5 - Descartar')),
                ('sample_6_weight', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Muestra 6 - Peso')),
                ('sample_6_law', models.CharField(max_length=200, verbose_name='Muestra 6 - Ley')),
                ('sample_6_discard', models.BooleanField(verbose_name='Muestra 6 - Descartar')),
                ('sample_7_weight', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Muestra 7 - Peso')),
                ('sample_7_law', models.CharField(max_length=200, verbose_name='Muestra 7 - Ley')),
                ('sample_7_discard', models.BooleanField(verbose_name='Muestra 7 - Descartar')),
                ('sample_8_weight', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Muestra 8 - Peso')),
                ('sample_8_law', models.CharField(max_length=200, verbose_name='Muestra 8 - Ley')),
                ('sample_8_discard', models.BooleanField(verbose_name='Muestra 8 - Descartar')),
                ('final_law', models.TextField(verbose_name='Ley Final')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.client', verbose_name='Cliente')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Gold',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(verbose_name='Número')),
                ('lot', models.IntegerField(verbose_name='Lote')),
                ('type', models.CharField(max_length=200, verbose_name='Tipo')),
                ('observations', models.TextField(null=True, verbose_name='Observaciones')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(auto_now_add=True)),
                ('witness', models.CharField(max_length=200, verbose_name='Testigo')),
                ('sample_1_reception_weight', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Muestra 1 - Peso Inicial')),
                ('sample_1_final_weight', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Muestra 1 - Peso Final')),
                ('sample_1_law', models.CharField(max_length=200, verbose_name='Muestra 1 - Ley')),
                ('sample_1_discard', models.BooleanField(verbose_name='Muestra 1 - Descartar')),
                ('sample_2_reception_weight', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Muestra 2 - Peso Inicial')),
                ('sample_2_final_weight', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Muestra 2 - Peso Final')),
                ('sample_2_law', models.CharField(max_length=200, verbose_name='Muestra 2 - Ley')),
                ('sample_2_discard', models.BooleanField(verbose_name='Muestra 2 - Descartar')),
                ('sample_3_reception_weight', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Muestra 3 - Peso Inicial')),
                ('sample_3_final_weight', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Muestra 3 - Peso Final')),
                ('sample_3_law', models.CharField(max_length=200, verbose_name='Muestra 3 - Ley')),
                ('sample_3_discard', models.BooleanField(verbose_name='Muestra 3 - Descartar')),
                ('sample_4_reception_weight', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Muestra 4 - Peso Inicial')),
                ('sample_4_final_weight', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Muestra 4 - Peso Final')),
                ('sample_4_law', models.CharField(max_length=200, verbose_name='Muestra 4 - Ley')),
                ('sample_4_discard', models.BooleanField(verbose_name='Muestra 4 - Descartar')),
                ('sample_5_reception_weight', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Muestra 5 - Peso Inicial')),
                ('sample_5_final_weight', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Muestra 5 - Peso Final')),
                ('sample_5_law', models.CharField(max_length=200, verbose_name='Muestra 5 - Ley')),
                ('sample_5_discard', models.BooleanField(verbose_name='Muestra 5 - Descartar')),
                ('sample_6_reception_weight', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Muestra 6 - Peso Inicial')),
                ('sample_6_final_weight', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Muestra 6 - Peso Final')),
                ('sample_6_law', models.CharField(max_length=200, verbose_name='Muestra 6 - Ley')),
                ('sample_6_discard', models.BooleanField(verbose_name='Muestra 6 - Descartar')),
                ('sample_7_reception_weight', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Muestra 7 - Peso Inicial')),
                ('sample_7_final_weight', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Muestra 7 - Peso Final')),
                ('sample_7_law', models.CharField(max_length=200, verbose_name='Muestra 7 - Ley')),
                ('sample_7_discard', models.BooleanField(verbose_name='Muestra 7 - Descartar')),
                ('sample_8_reception_weight', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Muestra 8 - Peso Inicial')),
                ('sample_8_final_weight', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Muestra 8 - Peso Final')),
                ('sample_8_law', models.CharField(max_length=200, verbose_name='Muestra 8 - Ley')),
                ('sample_8_discard', models.BooleanField(verbose_name='Muestra 8 - Descartar')),
                ('final_law', models.TextField(verbose_name='Ley final')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.client', verbose_name='Cliente')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]