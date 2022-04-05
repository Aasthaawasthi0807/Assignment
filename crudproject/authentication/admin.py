from django.contrib import admin
from .models import Books


# Register your models here.
@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):

    list_display = ('id','book_name','category','author','published_on')
    list_per_page = 10
    search_fields = ('author',)
    list_filter = ('category',)