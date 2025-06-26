from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import *
from django.contrib.auth import authenticate

class UsuarioSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='pk', read_only=True)
    rol_id = serializers.CharField(source='rol')

    class Meta:
        model = Usuario
        fields = ['id', 'correo', 'nombre_usuario', 'rol_id']

class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = '__all__'

class TableroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tablero
        fields = '__all__'

class TareasTableroSerializer(serializers.ModelSerializer):
    class Meta:
        model = TareasTablero
        fields = '__all__'

class EventoCalendarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventoCalendario
        fields = '__all__'

class ChatIASerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatIA
        fields = '__all__'

class ProgresoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Progreso
        fields = '__all__'

class RecordatorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recordatorio
        fields = '__all__'

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = Usuario.USERNAME_FIELD  # Esto ya es 'correo'

    def validate(self, attrs):
        correo = attrs.get("correo")
        password = attrs.get("password")

        if not correo or not password:
            raise serializers.ValidationError("Correo y contraseña son requeridos")

        user = authenticate(request=self.context.get('request'), username=correo, password=password)

        if user is None:
            raise serializers.ValidationError("Credenciales incorrectas")

        # Aquí se valida correctamente con el flujo original
        data = super().validate(attrs)

        data["id"] = user.id
        data["nombre_usuario"] = user.nombre_usuario
        data["rol"] = user.rol  # 👈 aquí agregas el campo rol
        return data
    
class UsuarioEditarSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)
    rol = serializers.CharField()  # <- CAMBIAR ESTO

    class Meta:
        model = Usuario
        fields = ['id', 'correo', 'nombre_usuario', 'rol', 'password']

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        rol = validated_data.pop('rol', None)  # ahora sí se recibe correctamente

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if rol:
            instance.rol = rol

        if password:
            instance.set_password(password)

        instance.save()
        return instance
