# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Genre'
        db.create_table('game_genre', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=2000)),
        ))
        db.send_create_signal('game', ['Genre'])

        # Adding model 'Game'
        db.create_table('game_game', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=254)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=500)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=2000)),
        ))
        db.send_create_signal('game', ['Game'])

        # Adding M2M table for field genre_set on 'Game'
        m2m_table_name = db.shorten_name('game_game_genre_set')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('game', models.ForeignKey(orm['game.game'], null=False)),
            ('genre', models.ForeignKey(orm['game.genre'], null=False))
        ))
        db.create_unique(m2m_table_name, ['game_id', 'genre_id'])

        # Adding model 'Snapshot'
        db.create_table('game_snapshot', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('game', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['game.Game'])),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=500)),
        ))
        db.send_create_signal('game', ['Snapshot'])

        # Adding model 'DownloadType'
        db.create_table('game_downloadtype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('game', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['game.Game'])),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('platform', self.gf('django.db.models.fields.CharField')(max_length=3)),
        ))
        db.send_create_signal('game', ['DownloadType'])


    def backwards(self, orm):
        # Deleting model 'Genre'
        db.delete_table('game_genre')

        # Deleting model 'Game'
        db.delete_table('game_game')

        # Removing M2M table for field genre_set on 'Game'
        db.delete_table(db.shorten_name('game_game_genre_set'))

        # Deleting model 'Snapshot'
        db.delete_table('game_snapshot')

        # Deleting model 'DownloadType'
        db.delete_table('game_downloadtype')


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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '254'})
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