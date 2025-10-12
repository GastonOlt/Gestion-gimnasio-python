from django.contrib import admin
from .models import  Servicio , Cliente

# Register your models here.

class ServicioAdmin(admin.ModelAdmin):
      list_display=('nombre','descripcion','precio','id')

class ClienteAdmin(admin.ModelAdmin):
      list_display=('nombre','apellido','fecha_registro','get_servicios','editado','imagen')
      list_filter=('servicios','fecha_registro')

      def get_servicios(self, obj):
         return ", ".join([servicio.nombre for servicio in obj.servicios.all()])
      get_servicios.short_description = 'Servicios'

admin.site.register(Servicio,ServicioAdmin)
admin.site.register(Cliente,ClienteAdmin)
