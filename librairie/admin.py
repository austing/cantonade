from django.contrib import admin

from librairie.models import Auteur, Tag, Texte

admin.site.register(Auteur)
admin.site.register(Tag)
admin.site.register(Texte)