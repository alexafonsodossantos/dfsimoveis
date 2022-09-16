from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from imoveis import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('detalhes/<int:imovel_id>', views.imovel, name='imovel'),
    path('cadastro', views.cadastro_imovel, name='cadastro'),
    path('salvar_imovel', views.salvar_imovel, name='salvar'),
    path('update_agent', views.update_agent, name='update_agent'),
]
urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)