from django.contrib import admin
from .models import CategoriaProd, Producto

class CategoriaProdAdmin(admin.ModelAdmin):
    readonly_fields = ('create', 'update')

class ProductoAdmin(admin.ModelAdmin):
    readonly_fields = ('create', 'update')
    

admin.site.register(CategoriaProd, CategoriaProdAdmin)
admin.site.register(Producto, ProductoAdmin)