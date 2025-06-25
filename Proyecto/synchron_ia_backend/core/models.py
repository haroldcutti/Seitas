from django.db import models

class Usuario(models.Model):
    nombre_completo = models.CharField(max_length=100)
    nombre_usuario = models.CharField(max_length=50, unique=True)
    correo = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre_usuario


class Tarea(models.Model):
    PRIORIDAD_CHOICES = [('ALTA', 'Alta'), ('MEDIA', 'Media'), ('BAJA', 'Baja')]
    TIPO_CHOICES = [('ACADEMICA', 'Académica'), ('PERSONAL', 'Personal')]

    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_vencimiento = models.DateField()
    prioridad = models.CharField(max_length=10, choices=PRIORIDAD_CHOICES)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    completada = models.BooleanField(default=False)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)


class Tablero(models.Model):
    TIPO_CHOICES = [('ACADEMICO', 'Académico'), ('PERSONAL', 'Personal')]

    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)


class TareasTablero(models.Model):
    tablero = models.ForeignKey(Tablero, on_delete=models.CASCADE)
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE)


class EventoCalendario(models.Model):
    titulo = models.CharField(max_length=100)
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)


class ChatIA(models.Model):
    mensaje_usuario = models.TextField()
    respuesta_ia = models.TextField()
    fecha = models.DateTimeField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)


class Progreso(models.Model):
    TIPO_CHOICES = [('ACADEMICA', 'Académica'), ('PERSONAL', 'Personal')]

    total_tareas = models.IntegerField()
    tareas_completadas = models.IntegerField()
    tipo_tarea = models.CharField(max_length=10, choices=TIPO_CHOICES)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)


class Recordatorio(models.Model):
    mensaje = models.TextField()
    fecha_creacion = models.DateTimeField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
