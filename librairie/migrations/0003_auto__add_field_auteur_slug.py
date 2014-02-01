# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Auteur.slug'
        db.add_column(u'librairie_auteur', 'slug',
                      self.gf('django.db.models.fields.CharField')(default='asdfasdf', max_length=255),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Auteur.slug'
        db.delete_column(u'librairie_auteur', 'slug')


    models = {
        u'librairie.auteur': {
            'Meta': {'object_name': 'Auteur'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'prenom': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'librairie.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        u'librairie.texte': {
            'Meta': {'object_name': 'Texte'},
            'auteur': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['librairie.Auteur']"}),
            'date_creation': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modification': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'html': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pdf': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['librairie.Tag']", 'symmetrical': 'False'}),
            'titre': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['librairie']