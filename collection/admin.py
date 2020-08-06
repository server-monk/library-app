from django.contrib import admin
from collection.models import Book

# Register your models here.


admin.site.register(Book)


# class BookAdmin(admin.ModelAdmin):
list_display = ('book_title', 'author', 'genre', 'is_available')
search_fields = ('book_title', 'author', 'genre')
ordering = 'book_id'
