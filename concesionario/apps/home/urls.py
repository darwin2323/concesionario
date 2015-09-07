from django.conf.urls.defaults import patterns, url

urlpatterns = patterns ('concesionario.apps.home.views',
	url(r'^$', 'index_view', name = 'vista_index'),
		#url index
	url(r'^auto/(?P<id_aut>.*)/$', 'single_auto_view', name = 'vista_single_auto'),
	url(r'^clientes/(?P<id_clientes>.*)/$', 'single_clientes_view', name = 'vista_single_clientes'),
	url(r'^ventas/(?P<id_ventas>.*)/$', 'single_ventas_view', name = 'vista_single_ventas'),
	url(r'^vendedor/(?P<id_vendedor>.*)/$', 'single_vendedor_view', name = 'vista_single_vendedor'),

	url(r'^autos/$', 'autos_view',name = 'vista_autos'),	
	url(r'^clientes/$','clientes_view',name = 'vista_clientes'),
	url(r'^ventas/$','ventas_view',name = 'vista_ventas'),
	url(r'^vendedores/$','vendedor_view',name = 'vista_vendedor'),
		# urls listar 
	url(r'^busqueda/$','busqueda_view', name = 'vista_busqueda'),
		#url de busqueda

	


)