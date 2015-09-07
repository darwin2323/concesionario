from django.db import models

# Create your models here.

class Auto(models.Model):
	def url(self, filname):
			ruta = "MultimediaData/Auto/%s/%s"%(self.nombre, str(filname))
			return ruta
	placa	  	= models.CharField(max_length = 6,unique = True) 
	nombre    	= models.CharField(max_length = 30)
	marca     	= models.CharField(max_length = 15)
	modelo    	= models.CharField(max_length = 15)
	color     	= models.CharField(max_length = 15)
	precio 	  	= models.IntegerField()# decimal_places = )
	imagen    	= models.ImageField(upload_to = url, null = True, blank = True)
	status	  	= models.BooleanField(default = True)
	def __unicode__(self):
		return self.marca

class Clientes(models.Model):
	cedula   	= models.CharField(max_length = 30,unique = True)
	nombre    	= models.CharField(max_length = 30)
	apellido    = models.CharField(max_length = 30)
	direccion	= models.CharField(max_length = 30)
	telefono  	= models.CharField(max_length = 10)
	email     	= models.EmailField(max_length = 30)

	def __unicode__(self):
		return self.nombre

class Vendedor(models.Model):
	cedula 	= models.CharField(max_length = 10,unique = True)
	nombre     	= models.CharField(max_length = 30)
	apellido    	= models.CharField(max_length = 30)
	direccion   = models.CharField(max_length = 50)
	telefono	= models.CharField(max_length = 15)
	status		= models.BooleanField(default = True)
	def __unicode__(self):
		return self.nombre


		

class Ventas(models.Model):
	Clientes   		= models.ForeignKey(Clientes)
	vendedor		= models.ForeignKey(Vendedor)
	fecha			= models.CharField(max_length = 30)
	Auto       		= models.ForeignKey(Auto)
	total_ventas 	= models.DecimalField(max_digits = 10, decimal_places = 3)
	def __unicode__(self ):
		return self.fecha
		 
		
		
	