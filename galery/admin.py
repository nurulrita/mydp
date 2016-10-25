from django.contrib import admin
from .models import Galery, Category

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    
admin.site.register(Galery)
admin.site.register(Category, CategoryAdmin)
