from django.urls import path, include
from .views import obtener_roles 
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'tareas', TareaViewSet)
router.register(r'tableros', TableroViewSet)
router.register(r'tareas-tablero', TareasTableroViewSet)
router.register(r'eventos', EventoCalendarioViewSet)
router.register(r'chats-ia', ChatIAViewSet)
router.register(r'progresos', ProgresoViewSet)
router.register(r'recordatorios', RecordatorioViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('roles/', obtener_roles),
]
