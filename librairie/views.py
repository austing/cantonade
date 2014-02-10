from django.shortcuts import render

from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from librairie.models import Auteur, Tag, Texte, IndexFlatPage

from datetime import datetime

class RecentTexteList(ListView):

    template_name = 'librairie/recent_textes.html'

    def get_context_data(self, **kwargs):
        context = super(RecentTexteList, self).get_context_data(**kwargs)
        context['flatpage'] = self.flatpage
        return context

    def get_queryset(self):
        self.flatpage = get_object_or_404(IndexFlatPage, url='/index/')
        return Texte.objects.filter(publique=True, date_de_publication__lte=datetime.now()).order_by('date_de_publication')

class AuteurTexteList(ListView):

    template_name = 'librairie/textes_par_auteur.html'

    def get_context_data(self, **kwargs):
        context = super(AuteurTexteList, self).get_context_data(**kwargs)
        context['auteur'] = self.auteur
        return context

    def get_queryset(self):
        self.auteur = get_object_or_404(Auteur, slug=self.args[0])
        return Texte.objects.filter(auteur=self.auteur)

class TagTexteList(ListView):

    template_name = 'librairie/textes_par_tag.html'

    def get_context_data(self, **kwargs):
        context = super(TagTexteList, self).get_context_data(**kwargs)
        context['tag'] = self.tag
        return context

    def get_queryset(self):
        self.tag = get_object_or_404(Tag, slug=self.args[0])
        return Texte.objects.filter(tags=self.tag)

class AuteurList(ListView):

    model = Auteur

class TagList(ListView):

    model = Tag

class TexteDetailView(DetailView):

    model = Texte