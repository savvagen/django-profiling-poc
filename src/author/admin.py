from django.contrib import admin
from .models import Author

# Register your models here.
# admin.site.register(Author)


# https://realpython.com/customize-django-admin-python/
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "name", "email" )