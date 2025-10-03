# mascotas/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contacto/', views.contacto, name='contacto'),
    path('adopcion/', views.adopcion, name='adopcion'),
    path('nosotros/', views.nosotros, name='nosotros'),
    # Un solo endpoint para crear solicitudes de adopción
    path('adoptar/', views.adoptar_modal, name='adoptar'),
]
