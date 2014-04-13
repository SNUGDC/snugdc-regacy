# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Role'
        db.create_table('role_role', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=254)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=2000)),
        ))
        db.send_create_signal('role', ['Role'])


    def backwards(self, orm):
        # Deleting model 'Role'
        db.delete_table('role_role')


    models = {
        'role.role': {
            'Meta': {'object_name': 'Role'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '254'})
        }
    }

    complete_apps = ['role']