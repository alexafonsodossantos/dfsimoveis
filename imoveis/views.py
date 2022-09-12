from django.shortcuts import render
from .models import Casa
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
# Create your views here.

def index(request):
    casas = Casa.objects.order_by('data_cadastro')
    template = loader.get_template('index.html')
    context = {
        'casas': casas,
    }
    return HttpResponse(template.render(context, request))

def imovel(request, imovel_id):
    imovel = get_object_or_404(Casa, pk=imovel_id)
    return render(request, 'detalhe_imovel.html', {'imovel': imovel})