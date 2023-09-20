from django.db import models
from django.utils import timezone

# Create your models here.

class equipamentos(models.Model):
    nome = models.CharField(max_length=100)
    imagem = models.CharField(max_length=200)
    descricao = models.CharField(max_length=200)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class usuarios(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField
    genero = models.CharField(max_length=10)
    nascimento = models.DateField
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class cargos(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class usuario_cargo(models.Model):
    usuario = models.ForeignKey(usuarios, related_name="usuario", on_delete=models.CASCADE)
    cargo = models.ForeignKey(cargos, related_name="cargo", on_delete=models.CASCADE)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class comentarios(models.Model):
    usuario = models.ForeignKey(usuario_cargo, related_name="usuario_cargo", on_delete=models.CASCADE)
    data = models.DateField(default=timezone.now())
    descricao = models.CharField(max_length=250)

    def __str__(self):
        return self.name



