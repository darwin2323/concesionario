# Create your views here.

from django.template import RequestContext
from django.shortcuts import render_to_response
from concesionario.apps.ventas.models import *
from concesionario.apps.ventas.forms import *
#from concesionario.apps.home.models import *
from django.http import HttpResponseRedirect

def add_auto_view(request):
	info = "inicializando"
	if request.method == "POST":
		formulario = add_auto_form(request.POST,request.FILES)
		if formulario.is_valid():
			add = formulario.save(commit = False)
			add.status = True
			add.save() #guarda la informacion
			formulario.save_m2m() #guarda las relaciones ManyToMany
			info = "Guardado Satisfactoriamente"
			return HttpResponseRedirect ('/auto/%s ' %add.id)
	else:
		formulario = add_auto_form()
	ctx ={ 'for':formulario,'informacion':info}# LA VARIABLE FORMULARIO ME LA LLAMA DESDE UN TEMPLATE DE AGREGAR
	return render_to_response('ventas/add_auto.html', ctx,context_instance = RequestContext(request))

def add_clientes_view(request):
	info = "inicializando"
	if request.method == "POST":
		formulario = add_clientes_form(request.POST,request.FILES)
		if formulario.is_valid():
			add = formulario.save(commit = False)
			add.save() #guarda la informacion
			formulario.save_m2m() #guarda las relaciones ManyToMany
			info = "Guardado Satisfactoriamente"
			return HttpResponseRedirect ('/clientes/%s ' %add.id)
	else:
		formulario = add_clientes_form()
	ctx ={ 'form':formulario,'informacion':info}
	return render_to_response('ventas/add_clientes.html', ctx,context_instance = RequestContext(request))

def add_ventas_view(request):
	info = "inicializando"
	if request.method == "POST":
		formulario = add_ventas_form(request.POST,request.FILES)
		if formulario.is_valid():
			add = formulario.save(commit = False)
			add.save() #guarda la informacion
			formulario.save_m2m() #guarda las relaciones ManyToMany
			info = "Guardado Satisfactoriamente"
			return HttpResponseRedirect ('/ventas/%s ' %add.id)
	else:
		formulario = add_ventas_form()
	ctx ={ 'form':formulario,'informacion':info}
	return render_to_response('ventas/add_ventas.html', ctx,context_instance = RequestContext(request))



def add_vendedor_view(request):
	info = "inicializando"
	if request.method == "POST":
		formulario = add_vendedor_form(request.POST,request.FILES)
		if formulario.is_valid():
			add = formulario.save(commit = False)
			add.save() #guarda la informacion
			add.status = True
			formulario.save_m2m() #guarda las relaciones ManyToMany
			info = "Guardado Satisfactoriamente"
			return HttpResponseRedirect ('/vendedor/%s ' %add.id)
	else:
		formulario = add_clientes_form()
	ctx ={ 'form':formulario,'informacion':info}
	return render_to_response('ventas/add_vendedor.html', ctx,context_instance = RequestContext(request))

def edit_auto_view(request,id_auto):
	info = ""
	auto = Auto.objects.get(pk = id_auto)
	if request.method == "POST":
		formulario = add_auto_form(request.POST, request.FILES, instance = auto)
		if formulario.is_valid():
			edit_auto = formulario.save(commit = False )
			formulario.save_m2m()
			edit_auto.status = True
			edit_auto.save()
			info = "Guardado Satisfactoriamente"
			return HttpResponseRedirect('/auto/%s'% edit_auto.id)
	else:
		formulario = add_auto_form(instance = auto)
	ctx = {'form': formulario, 'informacion':info}
	return render_to_response ('ventas/edit_auto.html', ctx, context_instance = RequestContext(request))


def edit_clientes_view(request, id_clientes):
	info = ""
	clientes= Clientes.objects.get(pk = id_clientes)
	if request.method == "POST":
		formulario = add_clientes_form(request.POST, request.FILES, instance = clientes)
		if formulario.is_valid():
			edit_clientes = formulario.save(commit = False )
			formulario.save_m2m()
			edit_clientes.save()
			info = "Guardado Satisfactoriamente"
			return HttpResponseRedirect('/cliente/%s'% edit_clientes.id)
	else:
		formulario = add_clientes_form(instance = clientes)
	ctx = {'form': formulario, 'informacion':info}
	return render_to_response ('ventas/edit_cliente.html', ctx, context_instance = RequestContext(request))


def edit_ventas_view(request, id_ventas):
	info = ""
	ventas = Ventas.objects.get(pk = id_ventas)
	if request.method == "POST":
		formulario = add_ventas_form(request.POST, request.FILES, instance = ventas)
		if formulario.is_valid():
			edit_ventas = formulario.save(commit = False )
			formulario.save_m2m()
			edit_ventas.save()
			info = "Guardado Satisfactoriamente"
			return HttpResponseRedirect('/ventas/%s'% edit_ventas.id)
	else:
		formulario = add_ventas_form(instance = ventas)
	ctx = {'form': formulario, 'informacion':info}
	return render_to_response ('ventas/edit_ventas.html', ctx, context_instance = RequestContext(request))


def edit_vendedor_view(request, id_vendedor):
	info = ""
	vendedor = Vendedor.objects.get(pk = id_vendedor)
	if request.method == "POST":
		formulario = add_vendedor_form(request.POST, request.FILES, instance = vendedor)
		if formulario.is_valid():
			edit_vendedor = formulario.save(commit = False )
			formulario.save_m2m()
			edit_vendedor.save()
			info = "Guardado Satisfactoriamente"
			return HttpResponseRedirect('/ventas/%s'% edit_vendedor.id)
	else:
		formulario = add_vendedor_form(instance = vendedor)
	ctx = {'form': formulario, 'informacion':info}
	return render_to_response ('ventas/edit_vendedor.html', ctx, context_instance = RequestContext(request))

def del_auto_view(request,id_auto):
	info = "inicializando"
	try:
		auto = Auto.objects.get(pk = id_auto)
		auto.delete()
		info = "Auto eliminado satisfacatoriamente"
		return HttpResponseRedirect('/autos/')
		
	except :
		info = "auto no se puede eliminar"

		return	HttpResponseRedirect('/autos/')


def del_clientes_view(request,id_clientes):
	info = "inicializando"
	try:
		clientes = Clientes.objects.get(pk = id_clientes)
		clientes.delete()
		info = "clientes eliminado satisfacatoriamente"
		return HttpResponseRedirect('/clientes/')
		
	except :
		info = "clientes no se puede eliminar"

		return	HttpResponseRedirect('/clientes/')

def del_ventas_view(request,id_ventas):
	info = "inicializando"
	try:
		ventas = Ventas.objects.get(pk = id_ventas)
		ventas.delete()
		info = "ventas eliminado satisfacatoriamente"
		return HttpResponseRedirect('/ventas/')
		
	except :
		info = "ventas no se puede eliminar"

		return	HttpResponseRedirect('/ventas/')


def del_vendedor_view(request,id_vendedor):
	info = "inicializando"
	try:
		vendedor = Vendedor.objects.get(pk = id_vendedor)
		vendedor.delete()
		info = "ventas eliminado satisfacatoriamente"
		return HttpResponseRedirect('/vendedores/')
		
	except :
		info = "vendedor no se puede eliminar"

		return	HttpResponseRedirect('/vendedores/')





