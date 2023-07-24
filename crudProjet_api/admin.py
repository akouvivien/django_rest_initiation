from django.contrib import admin

from crudProjet_api.models import Author, Book

# administrez vos models depuis l'interface admin.
admin.site.register(Author)
admin.site.register(Book)