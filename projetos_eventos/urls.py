from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from eventos_app.views import EventoViewSet, ParticipanteViewSet

router = DefaultRouter()
router.register(r'eventos', EventoViewSet)
router.register(r'participantes', ParticipanteViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  
]