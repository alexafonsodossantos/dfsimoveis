from django.db import models
from django.utils import timezone
# Create your models here.
from PIL import Image
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
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lng = models.DecimalField(max_digits=9, decimal_places=6)

    def save(self):
        super().save()  # saving image first

        img = Image.open(self.foto.path) # Open image using self

        if img.height > 600 or img.width > 800 or img.height < 600 or img.width < 800: 
            new_img = (800, 600)
            img.thumbnail(new_img)
            img.save(self.foto.path)  # saving image at the same path
