from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'equipamentos', equipamentosAPIView)
router.register(r'usuarios', usuariosAPIView)
router.register(r'cargos', cargosAPIView)
router.register(r'usuariocargo', usuariocargoAPIView)
router.register(r'comentarios', comentariosAPIView)

urlpatterns = router.urls
