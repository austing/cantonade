from django.contrib import admin

from librairie.models import Auteur, Tag, Texte, IndexFlatPage

from widgets import CKEditorWidget

from django import forms

class TexteAdminForm(forms.ModelForm):
    html = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Texte

class TexteAdmin(admin.ModelAdmin):
  form = TexteAdminForm

admin.site.register(Auteur)
admin.site.register(Tag)
admin.site.register(Texte, TexteAdmin)
admin.site.register(IndexFlatPage)