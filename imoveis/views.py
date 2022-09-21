from django.shortcuts import render
from .models import Casa, Cota
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
import locale
import re
import requests
#from bs4 import BeautifulSoup


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
    cota = Cota.objects.filter(valor__range=(imovel.valor, imovel.valor*2))[0]
    return render(request, 'detalhe_imovel.html', {'imovel': imovel, 'cota':cota})


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




def imoveis_filter(request):
    casas = Casa.objects.all()
    print(request.POST)

    dorms = request.POST.get('dorms')
    if int(dorms) > 0:
        casas = Casa.objects.filter(dormitorios = dorms)

        
    suites = request.POST.get('suites')
    if int(suites) > 0:
        casas = Casa.objects.filter(suites=suites)

    garagem = request.POST.get('garagem')
    if int(garagem) > 0:
        casas = Casa.objects.filter(vagas = garagem)

        
#   area_servico = request.POST.get('area_servico')
#   if area_servico == "1":
#       area_servico = True
#   else:
#       area_servico = False
#   
#   if area_servico:
#       casas = Casa.objects.filter(area_servico= True)
#
#   piscina = request.POST.get('piscina')
#   if piscina == "1":
#       piscina = True
#   else:
#       piscina = False
#
#   if piscina:
#       casas = Casa.objects.filter(piscina = True)
#   
#
#   churrasqueira = request.POST.get('churrasqueira')
#   if churrasqueira == "1":
#       churrasqueira = True
#   else:
#       churrasqueira = False
#
#   if churrasqueira:
#       casas = Casa.objects.filter(churrasqueira = True)
#
#   area_gourmet = request.POST.get('area_gourmet')
#   if area_gourmet == "1":
#       area_gourmet = True
#   else:
#       area_gourmet = False
#
#   if area_gourmet:
#       casas = Casa.objects.filter(area_gourmet = True)
#
#
#
#   fp_min = request.POST.get('fp_min')
#   fp_max = request.POST.get('fp_max')
#
#   #casas = Casa.objects.filter(valor__range=(fp_min, fp_max))
    
    
    
    
    
    template = loader.get_template('index.html')
    context = {
        'casas': casas,
    }
    return HttpResponse(template.render(context, request))







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


def update_agent(request):
#    class Cotas:
#        url = ""
#        carta = ""
#        credito = 0
#        entrada = 0
#        parcelas = ""
#        segmento = "Imóveis"
#        vencimento = ""
#        codigo = 0
#
#
#    locale.setlocale(locale.LC_MONETARY, "pt_BR.UTF-8")
#    headers = {
#        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
#    }
#
#    html_content = requests.get("https://contempladoschapeco.com.br/consorcio/imovel/", headers=headers).text
#    soup = BeautifulSoup(html_content,features="html.parser")
#    lista_maior = []
#    obj_list = []
#
#    table = soup.find_all('table')
#    tds = soup.find_all('td')
#
#    for a in tds:
#        data = a.contents
#        lista_maior.append(data)
#
#    chunks = [lista_maior[x:x+6] for x in range(0, len(lista_maior), 6)]
#
#    for a in chunks:
#        index = chunks.index(a)
#        obj = Cotas()
#        credito =  int(re.sub('\D','',a[0][0]))/100
#        entrada =   (int(re.sub('\D','',a[1][0]))/100) + (credito * 0.07)
#        try:
#            parcelas =  a[2][0] + " " + a[5][0]
#        except:
#            parcelas =  a[2][0]
#        finally:
#            administradora =  a[3][0]
#            vencimento = "Dia " + a[4][0][0:2]
#
#        obj.credito = credito
#        obj.carta = administradora
#        obj.entrada = entrada
#        obj.parcelas = parcelas
#        obj.vencimento = vencimento
#
#        if administradora == "Caixa":
#            obj.url = "https://www.contempladaaqui.com.br/wp-content/uploads/2021/05/caixa.png"
#        elif administradora == "Bradesco":
#            obj.url = "https://www.contempladaaqui.com.br/wp-content/uploads/2021/07/Bradesco.png"
#        elif administradora == "Itau":
#            obj.url = "https://www.contempladaaqui.com.br/wp-content/uploads/2021/07/Itau.png"
#        elif administradora == "Caixa | SX5":
#            obj.url = "https://www.contempladaaqui.com.br/wp-content/uploads/2021/05/caixa.png"
#        else:
#            obj.url = ""
#
#        obj.codigo  = 12585 + index
#        obj.credito = credito
#        obj.entrada = entrada
#        obj_list.append(obj)
#
#    for a in obj_list:
#        cota = Cota.objects.create(codigo = a.codigo, administradora = a.carta,
#        valor = a.credito, entrada = a.entrada, parcelas = a.parcelas, segmento = a.segmento, vencimento = a.vencimento, img = a.url  )


    return HttpResponse("Dados inseridos!")



