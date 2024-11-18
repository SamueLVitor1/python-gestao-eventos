from django.db import models

# Create your models here.
class Evento(models.Model):
    nome = models.CharField(max_length=100)
    data = models.DateField()
    local = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Participante(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    evento = models.ForeignKey(Evento, related_name='participantes', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome} ({self.email})"