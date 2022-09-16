from django.db import models
from django.utils import timezone
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys


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
    foto1 = models.ImageField(upload_to="imoveis/static/images")
    foto2 = models.ImageField(upload_to="imoveis/static/images")
    foto3 = models.ImageField(upload_to="imoveis/static/images")
    foto4 = models.ImageField(upload_to="imoveis/static/images")
    def save(self):
		#Opening the uploaded image
        fotos = [self.foto1, self.foto2, self.foto3, self.foto4]

        im = Image.open(fotos[0])

        output = BytesIO()

        #Resize/modify the image
        im = im.resize( (1024,768) )

        #after modifications, save it to the output
        im.save(output, format='JPEG', quality=100)
        output.seek(0)

        #change the imagefield value to be the newley modifed image value
        fotos1 = InMemoryUploadedFile(output,'ImageField', "%s.jpg" %fotos[0].name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)

        super(Casa,self).save()

        im = Image.open(self.foto2)

        output = BytesIO()

        #Resize/modify the image
        im = im.resize( (1024,768) )

        #after modifications, save it to the output
        im.save(output, format='JPEG', quality=100)
        output.seek(0)

        #change the imagefield value to be the newley modifed image value
        self.foto2 = InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.foto2.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)

        super(Casa,self).save()


        im = Image.open(self.foto3)

        output = BytesIO()

        #Resize/modify the image
        im = im.resize( (1024,768) )

        #after modifications, save it to the output
        im.save(output, format='JPEG', quality=100)
        output.seek(0)

        #change the imagefield value to be the newley modifed image value
        self.foto3 = InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.foto3.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)

        super(Casa,self).save()

        im = Image.open(self.foto4)

        output = BytesIO()

        #Resize/modify the image
        im = im.resize( (1024,768) )

        #after modifications, save it to the output
        im.save(output, format='JPEG', quality=100)
        output.seek(0)

        #change the imagefield value to be the newley modifed image value
        self.foto4 = InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.foto4.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)

        super(Casa,self).save()