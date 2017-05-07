from __future__ import unicode_literals

from django.db import models

#Clase estudio
class estudio(models.Model):
	nombre = models.CharField(max_length=200)
	
	def __unicode__(self):
		return self.nombre

#Clase art
class art(models.Model):
	nombre=models.CharField(max_length=200)
	
	def __unicode__(self):
		return self.nombre
		
#Clase juzgado
class juzgado(models.Model):
	nombre=models.CharField(max_length=200)
	direccion=models.CharField(max_length=100,null=True,blank=True)
	telefono=models.CharField(max_length=50, null=True,blank=True)

        def __unicode__(self):
            return self.nombre
		
#Clase Siniestro
class siniestro(models.Model):
    numero=models.CharField(max_length=200,null=False)

    def __unicode__(self):
        return self.numero

#Clase Caso
class caso(models.Model):
    numero=models.IntegerField()
    f=models.CharField(max_length=20)
    tribunal=models.ForeignKey(juzgado)
    jd=models.CharField('JD',max_length=100,null=False,blank=False)
    descripcion=models.CharField(max_length=200,null=False,blank=False)
    expediente=models.CharField(max_length=100,null=False,blank=False)

    def __unicode__(self):
        return self.numero
