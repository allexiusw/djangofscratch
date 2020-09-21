from django.contrib import admin
from djangofscratch.books.models import Publisher, Author, Book


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name')

class Bookdmin(admin.ModelAdmin):
    list_display = ('title', 'authors_list', 'publisher', 'publication_date')
    search_fields = ('title', 'publication_date')
    date_hierarchy = 'publication_date'
    ordering = ('title', )
    filter_horizontal = ('authors', )

admin.site.register(Publisher)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, Bookdmin)