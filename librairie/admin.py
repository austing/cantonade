from django.contrib import admin

from myproject.myapp.models import Auteur, Tag, Texte

admin.site.register(Auteur)
admin.site.register(Tag)
admin.site.register(Texte)