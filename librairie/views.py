from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.views.generic import ListView, DetailView
from librairie.models import Auteur, Tag, Texte, IndexFlatPage
from datetime import datetime
from django.contrib.admin.views.decorators import staff_member_required
from django.utils import timezone

class RecentTexteList(ListView):

    template_name = 'librairie/recent_textes.html'

    def get_context_data(self, **kwargs):
        context = super(RecentTexteList, self).get_context_data(**kwargs)
        context['flatpage'] = self.flatpage
        return context

    def get_queryset(self):
        self.flatpage = get_object_or_404(IndexFlatPage, url='/index/')
        now = timezone.now().astimezone(timezone.get_current_timezone())
        return Texte.objects.filter(publique=True, date_de_publication__lte=now).order_by('-date_de_publication')


class AuteurTexteList(ListView):

    template_name = 'librairie/textes_par_auteur.html'

    def get_context_data(self, **kwargs):
        context = super(AuteurTexteList, self).get_context_data(**kwargs)
        context['auteur'] = self.auteur
        return context

    def get_queryset(self):
        self.auteur = get_object_or_404(Auteur, slug=self.args[0])
        now = timezone.now().astimezone(timezone.get_current_timezone())
        return Texte.objects.filter(auteur=self.auteur, publique=True, date_de_publication__lte=now).order_by('-date_de_publication')

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

    queryset = Auteur.objects.all().extra(select={'imf': 'UPPER(nom)'}, order_by=['imf'])
    context_object_name = 'auteur_list'
    model = Texte


class TagList(ListView):

    queryset = Tag.objects.order_by('tag')
    context_object_name = 'tag_list'
    model = Texte


class TexteDetailView(DetailView):

    model = Texte

    def get_object(self):
        object = super(TexteDetailView, self).get_object()
        now = timezone.now().astimezone(timezone.get_current_timezone())
        if not object.visible and not self.request.user.is_staff:
            raise Http404
        return object

