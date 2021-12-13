from django.contrib import admin
from .models import Post, Categoria

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('create', 'update')

class PostAdamin(admin.ModelAdmin):
    model = Categoria
    readonly_fields = ('created', 'updated')


admin.site.register(Categoria, CategoriaAdmin) 
admin.site.register(Post, PostAdamin)