from django.shortcuts import render
from .models import Casa
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

def index(request):
    casas = Casa.objects.order_by('data_cadastro')
    template = loader.get_template('index.html')
    context = {
        'casas': casas,
    }
    return HttpResponse(template.render(context, request))
