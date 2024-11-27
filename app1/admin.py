from django.contrib import admin
from .models import Bautizo, Comunion, Confirmacion, Matrimonio, Defuncion, Sepultura


# Registro de modelos en el admin
admin.site.register(Bautizo)
admin.site.register(Comunion)
admin.site.register(Confirmacion)
admin.site.register(Matrimonio)
admin.site.register(Defuncion)
admin.site.register(Sepultura)
