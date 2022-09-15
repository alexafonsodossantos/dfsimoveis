from .models import Casa
from django import forms

class CadastroImovel(forms.ModelForm):
    class Meta:  
        model = Casa
        fields = '__all__'

    nome_exibicao = forms.CharField(label='Nome exibição',max_length=255)
    endereco  = forms.CharField(label='Endereço',max_length=255)
    bairro  = forms.CharField(label='Bairro', max_length=255)
    cidade  = forms.CharField(label='Cidade', max_length=255)
    valor  = forms.FloatField(label='Valor' )
    m2_construido = forms.IntegerField(label='Área construída')
    m2_total = forms.IntegerField(label='Área total')
    dormitorios = forms.IntegerField(label='Dormitórios')
    suites = forms.IntegerField(label='Suítes')
    vagas = forms.IntegerField(label='Vagas')
    area_servico = forms.BooleanField(label='Área de serviço', required=False, initial=False)
    churrasqueira = forms.BooleanField(label='Churrasqueira', required=False, initial=False)
    piscina = forms.BooleanField(label='Piscina', required=False, initial=False)
    area_gourmet = forms.BooleanField(label='Área gourmet', required=False, initial=False)
    descricao = forms.CharField(label='Descrição')
    foto = forms.ImageField(label='Foto')
    lat = forms.DecimalField(max_digits=9, decimal_places=6)
    lng = forms.DecimalField(max_digits=9, decimal_places=6)