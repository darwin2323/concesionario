from django.contrib import admin
from concesionario.apps.ventas.models import Auto , Ventas, Clientes , Vendedor

admin.site.register(Auto)
admin.site.register(Ventas)
admin.site.register(Vendedor)
admin.site.register(Clientes)