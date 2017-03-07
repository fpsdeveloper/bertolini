from __future__ import unicode_literals

from django.db import models

#Clase Estudio
class Estudio(models.Model):
	nombre = models.CharField(max_length=200)
	
	def __str__(self):
		return self.nombre
