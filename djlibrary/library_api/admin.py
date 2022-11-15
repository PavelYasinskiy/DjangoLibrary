from django.contrib import admin
from .models import Book, Author

class BookAdmin(admin.ModelAdmin):
    list_display = ('name', "author", "isbn", "year", "pages")

class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "surname", "birthday")

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
