from django.contrib import admin
from . models import Estados, Cidades, Bairros

# Register your models here.

admin.site.register(Estados)
admin.site.register(Cidades)
admin.site.register(Bairros)