from __future__ import unicode_literals

from django.db import models

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