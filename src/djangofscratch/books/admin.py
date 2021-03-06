from django.contrib import admin
from djangofscratch.books.models import Country, Publisher, Author, Book, Student


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name')

class Bookdmin(admin.ModelAdmin):
    list_display = ('title', 'authors_list', 'publisher', 'publication_date')
    search_fields = ('title', 'publication_date')
    date_hierarchy = 'publication_date'
    ordering = ('title', )
    filter_horizontal = ('authors', )
    fields = ('title', 'authors', 'publisher', )
    raw_id_fields = ('publisher', )

admin.site.register(Publisher)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, Bookdmin)
admin.site.register(Student)
admin.site.register(Country)