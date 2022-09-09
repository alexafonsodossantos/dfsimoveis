from django.db import models
from django.utils import timezone
# Create your models here.

class Casa(models.Model):
    id = models.BigAutoField(primary_key=True)
    data_cadastro = models.DateTimeField(default=timezone.now())
    nome_exibicao = models.CharField(max_length=255, null=True)
    endereco  = models.CharField(max_length=255, null=True)
    bairro  = models.CharField(max_length=255, null=True)
    cidade  = models.CharField(max_length=255, null=True)
    valor  = models.FloatField()
    m2_construido = models.IntegerField()
    m2_total = models.IntegerField()
    dormitorios = models.IntegerField()
    suites = models.IntegerField()
    vagas = models.IntegerField()
    area_servico = models.BooleanField()
    churrasqueira = models.BooleanField()
    piscina = models.BooleanField()
    area_gourmet = models.BooleanField()
    descricao = models.TextField()
    foto = models.ImageField(upload_to="imoveis/static/images")
