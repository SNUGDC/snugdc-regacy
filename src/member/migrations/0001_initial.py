# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Member'
        db.create_table('member_member', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=254)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=254, null=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=500)),
        ))
        db.send_create_signal('member', ['Member'])


    def backwards(self, orm):
        # Deleting model 'Member'
        db.delete_table('member_member')


    models = {
        'member.member': {
            'Meta': {'object_name': 'Member'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '500'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True'})
        }
    }

    complete_apps = ['member']