from django.contrib import admin
from .models import Producto



class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'temporada', 'precio', 'disponible', 'fecha_creacion')
    list_filter = ('categoria', 'temporada', 'disponible')
    search_fields = ('nombre', 'descripcion')
    list_editable = ('disponible', 'precio')
    ordering = ('categoria', 'nombre')

    list_per_page = 25

admin.site.register(Producto, ProductoAdmin)