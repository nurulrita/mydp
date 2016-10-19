from django.contrib import admin
from .models import Category, Page, Book, Author

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page)
admin.site.register(Book)
admin.site.register(Author)
