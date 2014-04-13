# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Participation'
        db.create_table('participation_participation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('member', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['member.Member'])),
            ('game', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['game.Game'])),
        ))
        db.send_create_signal('participation', ['Participation'])

        # Adding unique constraint on 'Participation', fields ['member', 'game']
        db.create_unique('participation_participation', ['member_id', 'game_id'])

        # Adding M2M table for field roles on 'Participation'
        m2m_table_name = db.shorten_name('participation_participation_roles')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('participation', models.ForeignKey(orm['participation.participation'], null=False)),
            ('role', models.ForeignKey(orm['role.role'], null=False))
        ))
        db.create_unique(m2m_table_name, ['participation_id', 'role_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'Participation', fields ['member', 'game']
        db.delete_unique('participation_participation', ['member_id', 'game_id'])

        # Deleting model 'Participation'
        db.delete_table('participation_participation')

        # Removing M2M table for field roles on 'Participation'
        db.delete_table(db.shorten_name('participation_participation_roles'))


    models = {
        'game.game': {
            'Meta': {'object_name': 'Game'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'genre_set': ('django.db.models.fields.related.ManyToManyField', [], {'null': 'True', 'to': "orm['game.Genre']", 'symmetrical': 'False'}),
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
        'member.member': {
            'Meta': {'object_name': 'Member'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '500'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            'title': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '254'})
        },
        'participation.participation': {
            'Meta': {'unique_together': "(('member', 'game'),)", 'object_name': 'Participation'},
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['game.Game']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'member': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['member.Member']"}),
            'roles': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['role.Role']", 'symmetrical': 'False'})
        },
        'role.role': {
            'Meta': {'object_name': 'Role'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '254'})
        }
    }

    complete_apps = ['participation']