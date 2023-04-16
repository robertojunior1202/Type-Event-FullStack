from django.contrib import admin

#Add a model Evento no Admin
from .models import Evento

admin.site.register(Evento)


