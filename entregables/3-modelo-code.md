Adjuntamos como entregable el modelo en código Python,  el cuál hace uso del ORM de Django para modelar y diseñar las entidades. El diagrama anterior (entregable nº _2) es una representación esquemática de este fragmento de código.

Las pocas funciones de acceso a los datos que encontramos en las clases del modelo representan operaciones atómicas o muy comunes, aquellas que requieren de relaciones entre varias entidades se encuentran dentro del módulo de servicios que contiene la aplicación.

```python

from django.db import models
from django.contrib.auth.models import User
from django.contrib.gis.db import models
from django.db.models import JSONField
from django.contrib.postgres.fields import ArrayField
from django.urls import reverse

from datetime import datetime, timedelta

class Cultivo(models.Model):

    nombre = models.CharField(max_length=20, primary_key=True)
    descripcion = models.CharField(max_length=200, null=True)
    es_variedad = models.ForeignKey('Cultivo', on_delete=models.CASCADE, null=True)

    def __str__(self):

        return self.nombre

class Indice(models.Model):

    nombre = models.TextField(max_length=100, primary_key=True)

    def __str__(self):

        return self.nombre

class Fenologico(models.Model):

    nombre = models.CharField(max_length=100, primary_key=True)
  
    def __str__(self):

        return self.nombre

class Estacion(models.Model):

    nombre = models.CharField(max_length=200, null=True)
    rango_it = models.FloatField(max_length=20, null=True)
    trilinea = ArrayField(ArrayField(models.FloatField(max_length=20, blank=True), size=15),size=3, null=True)

class Estacion_Historico(models.Model):

    id_auto = models.AutoField(primary_key=True)
    estacion = models.ForeignKey(Estacion, on_delete=models.CASCADE, null=True)
    fecha = models.DateField(null=True)
    file = models.CharField(max_length=10000)

class Parcela(models.Model):

    idx = models.BigIntegerField(primary_key=True)
    estacion = models.ForeignKey(Estacion, on_delete=models.CASCADE, null=True)
    municipio = models.CharField(max_length=200, null=True)
    parcela = models.CharField(max_length=200, null=True)

    altitud = models.FloatField(max_length=20, null=True)
    pendiente = models.FloatField(max_length=20, null=True)
    orientacion = models.FloatField(max_length=20, null=True)

    latest_ndvi = models.FloatField(max_length=20, null=True)
    geom = models.MultiPolygonField(srid=4326)
    geojson = JSONField(null=True)


    def get_absolute_url(self):

        return reverse('core:parcela_detail',   kwargs={"idx": self.idx})
        
    def update_ndvi(self, ndvi):

        self.latest_ndvi = ndvi
        self.save()

    def get_pixeles(self):
   
        return Pixel.objects.filter(parcela = self)
        
    def get_all_indices(self, indice_p):

        pixels = self.get_pixeles()
        return Mirar_Indice.objects.filter(pixel__in = pixels, indice = indice_p)

class Pixel (models.Model):

    ref     = models.BigAutoField(primary_key=True)
    idx     = models.BigIntegerField()
    parcela = models.ForeignKey(Parcela, on_delete=models.CASCADE, null=True)
    geom    = models.MultiPolygonField(srid=4326)
    geojson = JSONField(null=True)

class Campana (models.Model):

    anual = models.IntegerField()

class Predicciones (models.Model):

    parcela = models.ForeignKey(Parcela, on_delete=models.CASCADE, null=True)
    campana = models.ForeignKey(Campana, on_delete=models.CASCADE, null=True)
    calidad = models.FloatField(max_length=20)
    produccion = models.FloatField(max_length=20)

class Mirar_Fenologico(models.Model):

    parcela = models.ForeignKey(Parcela, on_delete=models.CASCADE, null=True)
    cultivo = models.ForeignKey(Cultivo, on_delete=models.CASCADE, null=True)
    estado = models.ForeignKey(Fenologico, on_delete=models.CASCADE)
    fecha = models.DateField(null=True)

class Mirar_Indice(models.Model):

    pixel   = models.ForeignKey(Pixel, on_delete=models.CASCADE, null=True)
    indice  = models.ForeignKey(Indice, on_delete=models.CASCADE, null=True)
    valor   = models.FloatField()
    fecha   = models.DateField(null=True)
    geojson = JSONField(null=True)
  
    def get_parcela(self):

        return Parcela.objects.get(idx = self.pixel)

    def get_historico_range(fecha_inicio, fecha_end):
    
        return Mirar_Indice.objects.filter(fecha__range=[fecha_inicio, fecha_end])

    def get_historico_parcela(parcela1):

        return Mirar_Indice.objects.filter(parcela = parcela1)

    def get_historico_parcela_range(parcela1, fecha_inicio, fecha_end):

        historico = Mirar_Indice.get_historico_range(fecha_inicio, fecha_end)
        
        return historico.filter(parcela = parcela1)

```
