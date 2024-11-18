from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from .models import Evento, Participante
from .serializers import EventoSerializer, ParticipanteSerializer

class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  #

class ParticipanteViewSet(viewsets.ModelViewSet):
    queryset = Participante.objects.all()
    serializer_class = ParticipanteSerializer