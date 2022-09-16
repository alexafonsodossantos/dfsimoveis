from django.shortcuts import render
from .models import Casa
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
# Create your views here.
from imoveis.forms import CadastroImovel
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


def cadastro_imovel(request):
    if request.method == 'POST':  
        form = CadastroImovel(request.POST, request.FILES)  
        if form.is_valid():  
            form.save()  
  
            # Getting the current instance object to display in the template  
            img_object = form.instance  
              
            return render(request, 'cadastro.html', {'form': form, 'img_obj': img_object})  
    else:  
        form = CadastroImovel()  
  
    return render(request, 'cadastro.html', {'form': form})  

def salvar_imovel(request):
    #query_dict = request.POST
    #print(query_dict)

    nome_exibicao = request.POST.get('nome_exibicao')
    endereco  = request.POST.get('endereco')
    bairro  = request.POST.get('bairro')
    cidade  = request.POST.get('cidade')
    valor  = request.POST.get('valor')
    m2_construido = request.POST.get('m2_construido')
    m2_total = request.POST.get('m2_total')
    dormitorios = request.POST.get('dormitorios')
    suites = request.POST.get('suites')
    vagas = request.POST.get('vagas')
    area_servico = request.POST.get('area_servico')
    
    if area_servico == "on":
        area_servico = True
    else:
        area_servico = False
    
    churrasqueira = request.POST.get('churrasqueira')
    
    if churrasqueira == 'on':
        churrasqueira = True
    else:
        churrasqueira = False

    piscina = request.POST.get('piscina')
    
    if piscina == 'on':
        piscina = True
    else:
        piscina = False
    
    area_gourmet = request.POST.get('area_gourmet')
    
    if area_gourmet == 'on':
        area_gourmet = True
    else:
        area_gourmet = False
    
    descricao = request.POST.get('descricao')
    foto1 = request.FILES.get('foto1')
    foto2 = request.FILES.get('foto2')
    foto3 = request.FILES.get('foto3')
    foto4 = request.FILES.get('foto4')
    lat = request.POST.get('lat')
    lng = request.POST.get('lng')

    Casa.objects.create(nome_exibicao=nome_exibicao, 
    endereco=endereco, 
    bairro=bairro,
    cidade=cidade,
    valor=valor, 
    m2_construido=m2_construido,
    m2_total=m2_total,
    dormitorios=dormitorios,
    suites=suites,
    vagas=vagas,
    area_servico=area_servico,
    churrasqueira=churrasqueira,
    piscina=piscina,
    area_gourmet=area_gourmet,
    descricao=descricao,
    foto1=foto1,
    foto2=foto2,
    foto3=foto3,
    foto4=foto4,
   )

    return HttpResponseRedirect('/')
