from django.contrib import admin
from django.urls import path, include

#Configuraoes para Aparecer as logos
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),
    path('eventos/', include('eventos.urls')),
    path('cliente/', include('cliente.urls')),
    
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) #Definindo URL para a midia (MEDIA_URL e MEDIA_ROOT está em Settings)
