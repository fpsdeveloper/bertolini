from __future__ import unicode_literals

from django.db import models

#Clase Persona
class persona(models.Model):
    tipoDocumento=models.CharField(max_length=10)
    numeroDocumento=models.CharField(max_length=100)
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=200)
    correo=models.CharField(max_length=250)

    def _str__(self):
        return self.nombre + ', ' + self.apellido

#Clase estudio
class estudio(models.Model):
	nombre = models.CharField(max_length=200)
	
	def __str__(self):
		return self.nombre

#Clase art
class art(models.Model):
	nombre=models.CharField(max_length=200)
	
	def __str__(self):
		return self.nombre;
		
#Clase agenda
class agenda(models.Model):
	
	def _str_(self):
		return 'agenda'
		
#Clase juzgado
class juzgado(models.Model):
	nombre=models.CharField(max_length=200)
	direccion=models.CharField(max_length=100)
	telefono=models.CharField(max_length=50)
		
#Clase audiencia
class audiencia(models.Model):	
	fecha = models.DateTimeField()
	juzgado = juzgado()	
	
#Clase Contacto	
class contacto(models.Model):
	nombre=models.CharField(max_length=200)
	direccion=models.CharField(max_length=100)
	telefono=models.CharField(max_length=50)
	correo=models.CharField(max_length=100)
	
	def _str_(self):
		return self.nombre

#Clase Caso
class caso(models.Model):
    numero=models.IntegerField()
    e=models.CharField(max_length=20)
    tribunal= juzgado()
    jd= models.IntegerField()
    titulo=models.CharField(max_length=200)
    expediente=models.CharField(max_length=100)
    siniestro=models.CharField(max_length=100)
    tipo=models.CharField(max_length=15)
    dni=models.CharField(max_length=200)
    montoDemanda=models.DecimalField(max_digits=12,decimal_places=2)
    incapacidadDemanda=models.DecimalField(max_digits=5,decimal_places=2)
    IBMDemanda=models.DecimalField(max_digits=12,decimal_places=2)
    contrato=models.CharField(max_length=50)
    fechaAccidente=models.DateField()
    fechaAlta=models.DateField()
    #Es un porcentaje? hay valores alfanumericos
    inscARTCM=models.CharField(max_length=20)

    def _str_(self):
        return self.numero
