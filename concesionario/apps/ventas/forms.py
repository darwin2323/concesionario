from concesionario.apps.ventas.models import *
from django import forms

class add_auto_form(forms.ModelForm):
	class Meta:
		model = Auto
		#se excluye el status por que en el modelo lo ponemos default=True
		exclude = {'status',}

class add_clientes_form(forms.ModelForm):
	class Meta:
		model = Clientes

		
class add_ventas_form(forms.ModelForm):
	class Meta:
		model = Ventas

class add_vendedor_form(forms.ModelForm):
	class Meta:
		model = Vendedor 
			

	
		