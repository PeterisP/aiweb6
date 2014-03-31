# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Person'
        db.create_table('team_person', (
            ('page_ptr', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, to=orm['pages.Page'], primary_key=True)),
            ('content', self.gf('mezzanine.core.fields.RichTextField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('initials', self.gf('django.db.models.fields.CharField')(null=True, blank=True, max_length=100)),
            ('position_en', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('position_lv', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('ailab_employee', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, to=orm['auth.User'])),
            ('researchgate_url', self.gf('django.db.models.fields.CharField')(null=True, blank=True, max_length=300)),
            ('linkedin_url', self.gf('django.db.models.fields.CharField')(null=True, blank=True, max_length=300)),
            ('scholar_url', self.gf('django.db.models.fields.CharField')(null=True, blank=True, max_length=300)),
        ))
        db.send_create_signal('team', ['Person'])


    def backwards(self, orm):
        # Deleting model 'Person'
        db.delete_table('team_person')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'unique': 'True'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'to': "orm['auth.Permission']", 'symmetrical': 'False'})
        },
        'auth.permission': {
            'Meta': {'object_name': 'Permission', 'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)"},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_set'", 'blank': 'True', 'to': "orm['auth.Group']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_set'", 'blank': 'True', 'to': "orm['auth.Permission']", 'symmetrical': 'False'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'db_table': "'django_content_type'", 'object_name': 'ContentType', 'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'pages.page': {
            'Meta': {'object_name': 'Page', 'ordering': "('titles',)"},
            '_meta_title': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '500'}),
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'content_model': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '50'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'expiry_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'gen_description': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_menus': ('mezzanine.pages.fields.MenusField', [], {'default': '(1,)', 'null': 'True', 'blank': 'True', 'max_length': '100'}),
            'in_sitemap': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'keywords_string': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '500'}),
            'login_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'children'", 'null': 'True', 'blank': 'True', 'to': "orm['pages.Page']"}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'short_url': ('django.db.models.fields.URLField', [], {'null': 'True', 'blank': 'True', 'max_length': '200'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '2000'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'titles': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '1000'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True'})
        },
        'sites.site': {
            'Meta': {'db_table': "'django_site'", 'object_name': 'Site', 'ordering': "('domain',)"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'team.person': {
            'Meta': {'object_name': 'Person', 'ordering': "('_order',)", '_ormbases': ['pages.Page']},
            'ailab_employee': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'content': ('mezzanine.core.fields.RichTextField', [], {}),
            'initials': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '100'}),
            'linkedin_url': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '300'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'to': "orm['pages.Page']", 'primary_key': 'True'}),
            'position_en': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'position_lv': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'researchgate_url': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '300'}),
            'scholar_url': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '300'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['team']