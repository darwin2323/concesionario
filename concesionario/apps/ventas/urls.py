from django.conf.urls.defaults import patterns, url
	
urlpatterns = patterns ('concesionario.apps.ventas.views',

	url(r'^add/auto/$','add_auto_view',name = 'vista_agregar_auto'),
	url(r'^add/clientes/$','add_clientes_view',name = 'vista_agregar_cliente'),
	url(r'^add/venta/$','add_ventas_view',name = 'vista_agregar_venta'),
	url(r'^add/vendedor/$','add_vendedor_view',name = 'vista_agregar_vendedor'),
	#urls editar
	url(r'^edit/auto/(?P<id_auto>.*)/$','edit_auto_view',name = 'vista_editar_auto'),
	url(r'^edit/cliente/(?P<id_clientes>.*)/$','edit_clientes_view',name = 'vista_editar_clientes'),
	url(r'^edit/ventas/(?P<id_ventas>.*)/$','edit_ventas_view',name = 'vista_editar_ventas'),
	url(r'^edit/vendedor/(?P<id_vendedor>.*)/$','edit_vendedor_view',name = 'vista_editar_vendedor'),
	#urls eliminar
	url(r'^del/autos/(?P<id_auto>.*)/$','del_auto_view',name = 'vista_eliminar_auto'),
	url(r'^del/clientes/(?P<id_clientes>.*)/$','del_clientes_view',name = 'vista_eliminar_cliente'),
	url(r'^del/ventas/(?P<id_ventas>.*)/$','del_ventas_view',name = 'vista_eliminar_venta'),
	url(r'^del/vendedor/(?P<id_vendedor>.*)/$','del_vendedor_view',name = 'vista_eliminar_vendedor'),



)
