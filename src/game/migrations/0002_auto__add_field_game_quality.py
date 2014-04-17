# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Game.quality'
        db.add_column('game_game', 'quality',
                      self.gf('django.db.models.fields.CharField')(max_length=1, default='L'),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Game.quality'
        db.delete_column('game_game', 'quality')


    models = {
        'game.downloadtype': {
            'Meta': {'object_name': 'DownloadType'},
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['game.Game']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'platform': ('django.db.models.fields.CharField', [], {'max_length': '3'})
        },
        'game.game': {
            'Meta': {'object_name': 'Game'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'genre_set': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['game.Genre']", 'symmetrical': 'False', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '500'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            'quality': ('django.db.models.fields.CharField', [], {'max_length': '1', 'default': "'L'"})
        },
        'game.genre': {
            'Meta': {'object_name': 'Genre'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'game.snapshot': {
            'Meta': {'object_name': 'Snapshot'},
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['game.Game']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '500'})
        }
    }

    complete_apps = ['game']