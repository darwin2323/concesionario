# Create your views here
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from concesionario.apps.ventas.models import *
from concesionario.apps.ventas.forms import *
from concesionario.apps.home.forms import *
def index_view(request):
	return render_to_response('home/index.html', context_instance = RequestContext(request))
	
def single_auto_view(request,id_aut):
	auto = Auto.objects.get(id = id_aut)# selciona desde auto where o donde auto.id = id_auto
	ctx  = {'au':auto}#mi variable de dicionario au me muestra los datos almacenados en la base de datos en el template por eso como la declaro aqui debo llamarla en mi ver de html.
	return render_to_response('home/single_auto.html',ctx,context_instance = RequestContext(request))
	
def autos_view(request):
	lista_auto = Auto.objects.all() 
	ctx = {'aut':lista_auto}# llamo mi dicionrio desde mi template de donde listo mis autos 
	return render_to_response('home/autos.html',ctx, context_instance = RequestContext(request))

def clientes_view(request):
	lista_clientes = Clientes.objects.all()
	ctx = {'clientes':lista_clientes}
	return render_to_response('home/clientes.html',ctx, context_instance = RequestContext(request))
	
def single_clientes_view(request,id_clientes):
	clientes = Clientes.objects.get(id = id_clientes)# selciona desde auto where o donde auto.id = id_auto
	ctx  = {'clientes':clientes}
	return render_to_response('home/single_clientes.html',ctx,context_instance = RequestContext(request))


def ventas_view(request):
	lista_ventas = Ventas.objects.all()
	ctx = {'ventas':lista_ventas}
	return render_to_response('home/ventas.html',ctx, context_instance = RequestContext(request))
	

def single_ventas_view(request,id_ventas):
	ventas = Ventas.objects.get(id = id_ventas)# selciona desde auto where o donde auto.id = id_auto
	ctx  = {'ventas':ventas}
	return render_to_response('home/single_ventas.html',ctx,context_instance = RequestContext(request))

def vendedor_view(request):
	lista_vendedor = Vendedor.objects.all()
	ctx = {'vendedor':lista_vendedor}
	return render_to_response('home/vendedor.html',ctx, context_instance = RequestContext(request))
	

def single_vendedor_view(request,id_vendedor):
	vendedor = Vendedor.objects.get(id = id_vendedor)# selciona desde auto where o donde auto.id = id_auto
	ctx  = {'vendedor':vendedor}
	return render_to_response('home/single_vendedor.html',ctx,context_instance = RequestContext(request))

def busqueda_view(request):
	if request.method == 'POST':#3
		formulario = busqueda_form(request.POST)
		if formulario.is_valid():
			b = formulario.cleaned_data['busqueda']
			ventas = Ventas.objects.filter(Clientes__cedula = b)
			cliente = Clientes.objects.filter(cedula = b)#2
			autos = Auto.objects.all()
			ctx = {'form': formulario, 'client':cliente,'venta': ventas, 'auto':autos}
			return render_to_response('home/busqueda.html',ctx, context_instance = RequestContext(request))
	else:
		formulario = busqueda_form()
	ctx = {'form': formulario}
	return render_to_response('home/busqueda.html',ctx , context_instance=RequestContext(request))