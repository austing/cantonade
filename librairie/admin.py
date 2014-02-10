from django.contrib import admin

from librairie.models import Auteur, Tag, Texte, IndexFlatPage

admin.site.register(Auteur)
admin.site.register(Tag)
admin.site.register(Texte)
admin.site.register(IndexFlatPage)