from django.contrib import admin
from .models import Galery, Category

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    
class GaleryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    
admin.site.register(Galery, GaleryAdmin)
admin.site.register(Category, CategoryAdmin)
