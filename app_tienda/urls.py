from django.urls import path
from . import views

app_name = 'app_tienda'

urlpatterns = [
    path('', views.ver_tiendas, name='ver_tiendas'),
    path('tienda/<int:tienda_id>/', views.info_tienda, name='info_tienda'),
    path('crear/', views.agregar_tienda, name='agregar_tienda'),
    path('editar/<int:tienda_id>/', views.editar_tienda, name='editar_tienda'),
    path('borrar/<int:tienda_id>/', views.borrar_tienda, name='borrar_tienda'),
]