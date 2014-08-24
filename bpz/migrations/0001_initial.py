# -*- coding: utf-8 -*-
# flake8: noqa
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'HomeOwnersAssociation'
        db.create_table(u'bpz_homeownersassociation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('object_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('hoa_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('geom', self.gf('django.contrib.gis.db.models.fields.GeometryField')()),
        ))
        db.send_create_signal(u'bpz', ['HomeOwnersAssociation'])

        # Adding model 'BOACase'
        db.create_table(u'bpz_boacase', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('object_id', self.gf('django.db.models.fields.IntegerField')()),
            ('case_id', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('hearing_date_str', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('geom', self.gf('django.contrib.gis.db.models.fields.GeometryField')()),
        ))
        db.send_create_signal(u'bpz', ['BOACase'])

        # Adding model 'TMAPCCase'
        db.create_table(u'bpz_tmapccase', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('object_id', self.gf('django.db.models.fields.IntegerField')()),
            ('case_id', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('case_type', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('hearing_date_str', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('geom', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')()),
        ))
        db.send_create_signal(u'bpz', ['TMAPCCase'])


    def backwards(self, orm):
        # Deleting model 'HomeOwnersAssociation'
        db.delete_table(u'bpz_homeownersassociation')

        # Deleting model 'BOACase'
        db.delete_table(u'bpz_boacase')

        # Deleting model 'TMAPCCase'
        db.delete_table(u'bpz_tmapccase')


    models = {
        u'bpz.boacase': {
            'Meta': {'object_name': 'BOACase'},
            'case_id': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'geom': ('django.contrib.gis.db.models.fields.GeometryField', [], {}),
            'hearing_date_str': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'bpz.homeownersassociation': {
            'Meta': {'object_name': 'HomeOwnersAssociation'},
            'geom': ('django.contrib.gis.db.models.fields.GeometryField', [], {}),
            'hoa_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'bpz.tmapccase': {
            'Meta': {'object_name': 'TMAPCCase'},
            'case_id': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'case_type': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'geom': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {}),
            'hearing_date_str': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        }
    }

    complete_apps = ['bpz']
