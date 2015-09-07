from django import forms


class busqueda_form(forms.Form):
	busqueda = forms.CharField(widget = forms.TextInput())
