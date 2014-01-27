from django.shortcuts import render

from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from librairie.models import Auteur, Tag, Texte

class AuteurTexteList(ListView):

    template_name = 'librairie/livres_par_auteur.html'

    def get_queryset(self):
        self.auteur = get_object_or_404(Auteur, name=self.args[0])
        return Texte.objects.filter(auteur=self.auteur)

class TagTexteList(ListView):

    template_name = 'librairie/livres_par_tag.html'

    def get_queryset(self):
        self.tag = get_object_or_404(Tag, name=self.args[0])
        return Texte.objects.filter(tag=self.tag)

class TexteDetailView(DetailView):

    model = Livre