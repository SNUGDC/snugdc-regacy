# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Game'
        db.create_table('game_game', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=254)),
            ('play_link', self.gf('django.db.models.fields.URLField')(max_length=200, null=True)),
            ('image', self.gf('django.db.models.fields.URLField')(max_length=200, null=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('game_type', self.gf('django.db.models.fields.CharField')(max_length=3)),
        ))
        db.send_create_signal('game', ['Game'])


    def backwards(self, orm):
        # Deleting model 'Game'
        db.delete_table('game_game')


    models = {
        'game.game': {
            'Meta': {'object_name': 'Game'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'game_type': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            'play_link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'})
        }
    }

    complete_apps = ['game']