from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Página principal
    path('archivos/', views.listar_archivos, name='listar_archivos'),
    path('archivo/<str:nombre_archivo>/', views.leer_archivo, name='leer_archivo'),
]
