from django.contrib import admin
from .models import Genre, Page, Book, Author

class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Genre, GenreAdmin)
admin.site.register(Page)
admin.site.register(Book)
admin.site.register(Author)
