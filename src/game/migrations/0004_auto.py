# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing M2M table for field genre on 'Game'
        db.delete_table(db.shorten_name('game_game_genre'))

        # Adding M2M table for field genre_set on 'Game'
        m2m_table_name = db.shorten_name('game_game_genre_set')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('game', models.ForeignKey(orm['game.game'], null=False)),
            ('genre', models.ForeignKey(orm['game.genre'], null=False))
        ))
        db.create_unique(m2m_table_name, ['game_id', 'genre_id'])


    def backwards(self, orm):
        # Adding M2M table for field genre on 'Game'
        m2m_table_name = db.shorten_name('game_game_genre')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('game', models.ForeignKey(orm['game.game'], null=False)),
            ('genre', models.ForeignKey(orm['game.genre'], null=False))
        ))
        db.create_unique(m2m_table_name, ['game_id', 'genre_id'])

        # Removing M2M table for field genre_set on 'Game'
        db.delete_table(db.shorten_name('game_game_genre_set'))


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
            'genre_set': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'null': 'True', 'to': "orm['game.Genre']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '500'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '254'})
        },
        'game.genre': {
            'Meta': {'object_name': 'Genre'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['game']