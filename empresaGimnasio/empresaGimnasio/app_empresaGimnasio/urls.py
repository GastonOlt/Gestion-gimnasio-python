from django.urls import path
from app_empresaGimnasio import views

urlpatterns =[
    path('',views.index,name='index'),
    path('listado/',views.listado,name='listado'),
    path('nuevo_cliente/',views.nuevo_cliente,name='nuevo_cliente'),
    path('listadoServicio/',views.listadoServicio,name='listadoServicio'),
    path('editar/<int:id>/',views.editar_cliente, name='editar_cliente'),
    path('eliminar/<int:id>/',views.eliminar_cliente, name="eliminar_cliente"),
    path('preguntasFrecu/',views.preuntasFrecu, name='preguntasFrecu')
]