from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
def obtener_roles(request):
    roles = [rol for rol, _ in Usuario.ROL_CHOICES]
    return Response(roles)

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return UsuarioEditarSerializer
        return UsuarioSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if not serializer.is_valid():
            print("Errores de validación:", serializer.errors)  # <-- 🔍 IMPORTANTE
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        self.perform_update(serializer)
        return Response(serializer.data)

class TareaViewSet(viewsets.ModelViewSet):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer

class TableroViewSet(viewsets.ModelViewSet):
    queryset = Tablero.objects.all()
    serializer_class = TableroSerializer

class TareasTableroViewSet(viewsets.ModelViewSet):
    queryset = TareasTablero.objects.all()
    serializer_class = TareasTableroSerializer

class EventoCalendarioViewSet(viewsets.ModelViewSet):
    queryset = EventoCalendario.objects.all()
    serializer_class = EventoCalendarioSerializer

class ChatIAViewSet(viewsets.ModelViewSet):
    queryset = ChatIA.objects.all()
    serializer_class = ChatIASerializer

class ProgresoViewSet(viewsets.ModelViewSet):
    queryset = Progreso.objects.all()
    serializer_class = ProgresoSerializer

class RecordatorioViewSet(viewsets.ModelViewSet):
    queryset = Recordatorio.objects.all()
    serializer_class = RecordatorioSerializer

class CurrentUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UsuarioSerializer(request.user)
        return Response(serializer.data)