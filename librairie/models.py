from django.db import models
from datetime import datetime
from django.contrib.flatpages.models import FlatPage

class IndexFlatPage(FlatPage):
    subtitle = models.TextField(verbose_name="deuxieme titre", blank=True, null=True)

class Auteur(models.Model):
    nom=models.CharField(max_length=255)
    prenom=models.CharField(max_length=255, blank=True, null=True)
    slug=models.CharField(max_length=255)
    bio=models.TextField(blank=True, null=True)

    def __unicode__(self):
        if self.prenom:
            return self.nom+', '+self.prenom
        else:
            return self.nom

class Tag(models.Model):
    tag=models.CharField(max_length=255)
    slug=models.CharField(max_length=255, unique=True)

    def __unicode__(self):
        return self.tag

class Texte(models.Model):
    auteur=models.ForeignKey(Auteur)
    titre=models.CharField(max_length=255)
    slug=models.CharField(max_length=255)
    description=models.TextField(blank=True, null=True)
    tags=models.ManyToManyField(Tag)
    html = models.FileField(upload_to="livres-html", blank=True, null=True)
    pdf = models.FileField(upload_to="livres-pdf", blank=True, null=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)
    publique = models.BooleanField(default=False)
    date_de_publication = models.DateTimeField(default=datetime.now, blank=True, null=True)

    def __unicode__(self):
        return self.titre+' ('+str(self.auteur)+')'