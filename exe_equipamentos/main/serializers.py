from rest_framework import serializers
from .models import *

class equipamentosSerializer(serializers.ModelSerializer):
    class Meta:
        model = equipamentos
        fields = '__all__'
        many = True

class usuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = usuarios
        fields = '__all__'
        many = True

class cargosSerializer(serializers.ModelSerializer):
    class Meta:
        model = cargos
        fields = '__all__'
        many = True

class usuariocargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = usuario_cargo
        fields = '__all__'
        many = True

class comentariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = comentarios
        fields = '__all__'
        many = True