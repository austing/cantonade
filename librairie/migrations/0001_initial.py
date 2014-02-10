# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'IndexFlatPage'
        db.create_table(u'librairie_indexflatpage', (
            (u'flatpage_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['flatpages.FlatPage'], unique=True, primary_key=True)),
            ('subtitle', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'librairie', ['IndexFlatPage'])

        # Adding model 'Auteur'
        db.create_table(u'librairie_auteur', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('prenom', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('bio', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'librairie', ['Auteur'])

        # Adding model 'Tag'
        db.create_table(u'librairie_tag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tag', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
        ))
        db.send_create_signal(u'librairie', ['Tag'])

        # Adding model 'Texte'
        db.create_table(u'librairie_texte', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('auteur', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['librairie.Auteur'])),
            ('titre', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('html', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('pdf', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('date_creation', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_modification', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('publique', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('date_de_publication', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, null=True, blank=True)),
        ))
        db.send_create_signal(u'librairie', ['Texte'])

        # Adding M2M table for field tags on 'Texte'
        m2m_table_name = db.shorten_name(u'librairie_texte_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('texte', models.ForeignKey(orm[u'librairie.texte'], null=False)),
            ('tag', models.ForeignKey(orm[u'librairie.tag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['texte_id', 'tag_id'])


    def backwards(self, orm):
        # Deleting model 'IndexFlatPage'
        db.delete_table(u'librairie_indexflatpage')

        # Deleting model 'Auteur'
        db.delete_table(u'librairie_auteur')

        # Deleting model 'Tag'
        db.delete_table(u'librairie_tag')

        # Deleting model 'Texte'
        db.delete_table(u'librairie_texte')

        # Removing M2M table for field tags on 'Texte'
        db.delete_table(db.shorten_name(u'librairie_texte_tags'))


    models = {
        u'flatpages.flatpage': {
            'Meta': {'ordering': "(u'url',)", 'object_name': 'FlatPage', 'db_table': "u'django_flatpage'"},
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'enable_comments': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'registration_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sites': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['sites.Site']", 'symmetrical': 'False'}),
            'template_name': ('django.db.models.fields.CharField', [], {'max_length': '70', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'})
        },
        u'librairie.auteur': {
            'Meta': {'object_name': 'Auteur'},
            'bio': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'prenom': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'librairie.indexflatpage': {
            'Meta': {'ordering': "(u'url',)", 'object_name': 'IndexFlatPage', '_ormbases': [u'flatpages.FlatPage']},
            u'flatpage_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['flatpages.FlatPage']", 'unique': 'True', 'primary_key': 'True'}),
            'subtitle': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'librairie.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'librairie.texte': {
            'Meta': {'object_name': 'Texte'},
            'auteur': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['librairie.Auteur']"}),
            'date_creation': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_de_publication': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'blank': 'True'}),
            'date_modification': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'html': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pdf': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'publique': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['librairie.Tag']", 'symmetrical': 'False'}),
            'titre': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['librairie']