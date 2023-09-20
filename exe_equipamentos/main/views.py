from .models import *
from .serializers import *
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class equipamentosAPIView(ModelViewSet):
   queryset = equipamentos.objects.all() #informa p/ a lib qual as consultas a serem feitas
   serializer_class = equipamentosSerializer #informa o serializer
   filter_backends = [DjangoFilterBackend] #usa a lib django-filter
   filterset_fields = ['nome',]
   permission_classes = (IsAuthenticated,)

class usuariosAPIView(ModelViewSet):
    queryset = usuarios.objects.all() #informa p/ a lib qual as consultas a serem feitas
    serializer_class = usuariosSerializer #informa o serializer
    filter_backends = [DjangoFilterBackend] #usa a lib django-filter
    filterset_fields = ['nome',]
    permission_classes = (IsAuthenticated,)

class cargosAPIView(ModelViewSet):
   queryset = cargos.objects.all() #informa p/ a lib qual as consultas a serem feitas
   serializer_class = cargosSerializer #informa o serializer
   filter_backends = [DjangoFilterBackend] #usa a lib django-filter
   filterset_fields = ['nome',]
   permission_classes = (IsAuthenticated,)

class usuariocargoAPIView(ModelViewSet):
   queryset = usuario_cargo.objects.all() #informa p/ a lib qual as consultas a serem feitas
   serializer_class = usuariocargoSerializer #informa o serializer
   filter_backends = [DjangoFilterBackend] #usa a lib django-filter
   filterset_fields = ['usuario',]
   permission_classes = (IsAuthenticated,)

class comentariosAPIView(ModelViewSet):
   queryset = comentarios.objects.all() #informa p/ a lib qual as consultas a serem feitas
   serializer_class = comentariosSerializer #informa o serializer
   filter_backends = [DjangoFilterBackend] #usa a lib django-filter
   filterset_fields = ['data',]
   permission_classes = (IsAuthenticated,)






