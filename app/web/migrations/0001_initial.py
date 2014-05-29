# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Feedback'
        db.create_table(u'web_feedback', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'], null=True)),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')(null=True)),
            ('kind', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('weight', self.gf('django.db.models.fields.IntegerField')()),
            ('notes', self.gf('django.db.models.fields.CharField')(max_length=512, blank=True)),
            ('posted', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('posted_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='feedbacks_posted', to=orm['web.UserProfile'])),
        ))
        db.send_create_signal(u'web', ['Feedback'])

        # Adding model 'Image'
        db.create_table(u'web_image', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('posted', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('posted_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='posted_images', to=orm['web.UserProfile'])),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('source_url', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('width', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True)),
            ('height', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True)),
            ('size', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'], null=True)),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')(null=True)),
        ))
        db.send_create_signal(u'web', ['Image'])

        # Adding model 'UserProfile'
        db.create_table(u'web_userprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(related_name='profile', unique=True, to=orm['auth.User'])),
            ('story', self.gf('django.db.models.fields.CharField')(max_length=512, null=True, blank=True)),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('last_updated_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', null=True, to=orm['web.UserProfile'])),
            ('location', self.gf('django.contrib.gis.db.models.fields.PointField')()),
            ('distance', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'web', ['UserProfile'])

        # Adding model 'ProfileOrganization'
        db.create_table(u'web_profileorganization', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.UserProfile'])),
            ('organization', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.Organization'])),
            ('role', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'web', ['ProfileOrganization'])

        # Adding model 'Organization'
        db.create_table(u'web_organization', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('logo', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['web.Image'], unique=True, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('last_updated_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', null=True, to=orm['web.UserProfile'])),
        ))
        db.send_create_signal(u'web', ['Organization'])

        # Adding model 'Pet'
        db.create_table(u'web_pet', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pet_type', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='pets_located_here', null=True, to=orm['web.Location'])),
            ('story', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('last_updated_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', null=True, to=orm['web.UserProfile'])),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', null=True, to=orm['web.UserProfile'])),
            ('thumbnail', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['web.Image'])),
            ('rescued_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='rescued_pets', null=True, to=orm['web.Organization'])),
            ('transport', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='manifest', null=True, to=orm['web.Transport'])),
        ))
        db.send_create_signal(u'web', ['Pet'])

        # Adding model 'PetAttribute'
        db.create_table(u'web_petattribute', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pet', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.Pet'])),
            ('attribute', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.Attribute'])),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('last_updated_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['web.UserProfile'])),
        ))
        db.send_create_signal(u'web', ['PetAttribute'])

        # Adding model 'Attribute'
        db.create_table(u'web_attribute', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('kind', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('attribute', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('display_name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('special_choices', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
            ('special_validation', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('last_updated_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['web.UserProfile'])),
        ))
        db.send_create_signal(u'web', ['Attribute'])

        # Adding model 'Location'
        db.create_table(u'web_location', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('geo', self.gf('django.contrib.gis.db.models.fields.PointField')()),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
        ))
        db.send_create_signal(u'web', ['Location'])

        # Adding model 'SegmentRoles'
        db.create_table(u'web_segmentroles', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('segment', self.gf('django.db.models.fields.related.OneToOneField')(related_name='volunteers', unique=True, to=orm['web.TransportSegment'])),
            ('role', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('priority', self.gf('django.db.models.fields.IntegerField')()),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=4)),
        ))
        db.send_create_signal(u'web', ['SegmentRoles'])

        # Adding M2M table for field user on 'SegmentRoles'
        m2m_table_name = db.shorten_name(u'web_segmentroles_user')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('segmentroles', models.ForeignKey(orm[u'web.segmentroles'], null=False)),
            ('userprofile', models.ForeignKey(orm[u'web.userprofile'], null=False))
        ))
        db.create_unique(m2m_table_name, ['segmentroles_id', 'userprofile_id'])

        # Adding model 'TransportSegment'
        db.create_table(u'web_transportsegment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sequence', self.gf('django.db.models.fields.IntegerField')()),
            ('pick_up_location', self.gf('django.db.models.fields.related.ForeignKey')(related_name='pickup+', to=orm['web.Location'])),
            ('drop_off_location', self.gf('django.db.models.fields.related.ForeignKey')(related_name='dropoff+', to=orm['web.Location'])),
            ('pick_up_datetime', self.gf('django.db.models.fields.DateTimeField')()),
            ('drop_off_datetime', self.gf('django.db.models.fields.DateTimeField')()),
            ('duration', self.gf('django.db.models.fields.TimeField')()),
            ('miles', self.gf('django.db.models.fields.IntegerField')()),
            ('transport', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='segments', null=True, to=orm['web.Transport'])),
            ('status', self.gf('django.db.models.fields.CharField')(default='ONTM', max_length=4)),
            ('offset', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('notes', self.gf('django.db.models.fields.CharField')(max_length=512, null=True, blank=True)),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('last_updated_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['web.UserProfile'])),
        ))
        db.send_create_signal(u'web', ['TransportSegment'])

        # Adding model 'Transport'
        db.create_table(u'web_transport', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('shipper', self.gf('django.db.models.fields.related.ForeignKey')(related_name='packages_shipped', to=orm['web.UserProfile'])),
            ('receiver', self.gf('django.db.models.fields.related.ForeignKey')(related_name='packages_received', to=orm['web.UserProfile'])),
            ('tracking_number', self.gf('django.db.models.fields.CharField')(default='PT02UHMD6OUND0B', unique=True, max_length=30)),
            ('notes', self.gf('django.db.models.fields.CharField')(max_length=512, null=True, blank=True)),
            ('status', self.gf('django.db.models.fields.CharField')(default='NEW', max_length=4)),
            ('started_on', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('start_location', self.gf('django.db.models.fields.related.ForeignKey')(related_name='start_location+', null=True, to=orm['web.Location'])),
            ('finished_on', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('finish_location', self.gf('django.db.models.fields.related.ForeignKey')(related_name='finish_location+', null=True, to=orm['web.Location'])),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['web.UserProfile'])),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('last_updated_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['web.UserProfile'])),
        ))
        db.send_create_signal(u'web', ['Transport'])

        # Adding model 'TransportLogEntry'
        db.create_table(u'web_transportlogentry', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('shipment', self.gf('django.db.models.fields.related.ForeignKey')(related_name='log_entries', to=orm['web.Transport'])),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')()),
            ('image', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['web.Image'], unique=True, null=True, blank=True)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=512, null=True, blank=True)),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('last_updated_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['web.UserProfile'])),
        ))
        db.send_create_signal(u'web', ['TransportLogEntry'])


    def backwards(self, orm):
        # Deleting model 'Feedback'
        db.delete_table(u'web_feedback')

        # Deleting model 'Image'
        db.delete_table(u'web_image')

        # Deleting model 'UserProfile'
        db.delete_table(u'web_userprofile')

        # Deleting model 'ProfileOrganization'
        db.delete_table(u'web_profileorganization')

        # Deleting model 'Organization'
        db.delete_table(u'web_organization')

        # Deleting model 'Pet'
        db.delete_table(u'web_pet')

        # Deleting model 'PetAttribute'
        db.delete_table(u'web_petattribute')

        # Deleting model 'Attribute'
        db.delete_table(u'web_attribute')

        # Deleting model 'Location'
        db.delete_table(u'web_location')

        # Deleting model 'SegmentRoles'
        db.delete_table(u'web_segmentroles')

        # Removing M2M table for field user on 'SegmentRoles'
        db.delete_table(db.shorten_name(u'web_segmentroles_user'))

        # Deleting model 'TransportSegment'
        db.delete_table(u'web_transportsegment')

        # Deleting model 'Transport'
        db.delete_table(u'web_transport')

        # Deleting model 'TransportLogEntry'
        db.delete_table(u'web_transportlogentry')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'web.attribute': {
            'Meta': {'object_name': 'Attribute'},
            'attribute': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kind': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'last_updated_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['web.UserProfile']"}),
            'pets': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['web.Pet']", 'through': u"orm['web.PetAttribute']", 'symmetrical': 'False'}),
            'special_choices': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'special_validation': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'})
        },
        u'web.feedback': {
            'Meta': {'object_name': 'Feedback'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kind': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'notes': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'posted': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'posted_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'feedbacks_posted'", 'to': u"orm['web.UserProfile']"}),
            'weight': ('django.db.models.fields.IntegerField', [], {})
        },
        u'web.image': {
            'Meta': {'object_name': 'Image'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']", 'null': 'True'}),
            'height': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'posted': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'posted_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'posted_images'", 'to': u"orm['web.UserProfile']"}),
            'size': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'source_url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'width': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'})
        },
        u'web.location': {
            'Meta': {'object_name': 'Location'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'geo': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'web.organization': {
            'Meta': {'object_name': 'Organization'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'last_updated_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'null': 'True', 'to': u"orm['web.UserProfile']"}),
            'logo': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['web.Image']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        u'web.pet': {
            'Meta': {'object_name': 'Pet'},
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'null': 'True', 'to': u"orm['web.UserProfile']"}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'last_updated_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'null': 'True', 'to': u"orm['web.UserProfile']"}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'pets_located_here'", 'null': 'True', 'to': u"orm['web.Location']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'pet_type': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'rescued_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'rescued_pets'", 'null': 'True', 'to': u"orm['web.Organization']"}),
            'story': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'thumbnail': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['web.Image']"}),
            'transport': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'manifest'", 'null': 'True', 'to': u"orm['web.Transport']"})
        },
        u'web.petattribute': {
            'Meta': {'object_name': 'PetAttribute'},
            'attribute': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['web.Attribute']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'last_updated_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['web.UserProfile']"}),
            'pet': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['web.Pet']"}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'web.profileorganization': {
            'Meta': {'object_name': 'ProfileOrganization'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'organization': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['web.Organization']"}),
            'role': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['web.UserProfile']"})
        },
        u'web.segmentroles': {
            'Meta': {'object_name': 'SegmentRoles'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'priority': ('django.db.models.fields.IntegerField', [], {}),
            'role': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'segment': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'volunteers'", 'unique': 'True', 'to': u"orm['web.TransportSegment']"}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'user': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'+'", 'symmetrical': 'False', 'to': u"orm['web.UserProfile']"})
        },
        u'web.transport': {
            'Meta': {'object_name': 'Transport'},
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['web.UserProfile']"}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'finish_location': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'finish_location+'", 'null': 'True', 'to': u"orm['web.Location']"}),
            'finished_on': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'last_updated_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['web.UserProfile']"}),
            'notes': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'receiver': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'packages_received'", 'to': u"orm['web.UserProfile']"}),
            'shipper': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'packages_shipped'", 'to': u"orm['web.UserProfile']"}),
            'start_location': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'start_location+'", 'null': 'True', 'to': u"orm['web.Location']"}),
            'started_on': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'NEW'", 'max_length': '4'}),
            'tracking_number': ('django.db.models.fields.CharField', [], {'default': "'PT0FCVPFGV4FM5C'", 'unique': 'True', 'max_length': '30'})
        },
        u'web.transportlogentry': {
            'Meta': {'object_name': 'TransportLogEntry'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['web.Image']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'last_updated_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['web.UserProfile']"}),
            'shipment': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'log_entries'", 'to': u"orm['web.Transport']"}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'web.transportsegment': {
            'Meta': {'object_name': 'TransportSegment'},
            'drop_off_datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'drop_off_location': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'dropoff+'", 'to': u"orm['web.Location']"}),
            'duration': ('django.db.models.fields.TimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'last_updated_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['web.UserProfile']"}),
            'miles': ('django.db.models.fields.IntegerField', [], {}),
            'notes': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'offset': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'pick_up_datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'pick_up_location': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'pickup+'", 'to': u"orm['web.Location']"}),
            'sequence': ('django.db.models.fields.IntegerField', [], {}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'ONTM'", 'max_length': '4'}),
            'transport': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'segments'", 'null': 'True', 'to': u"orm['web.Transport']"})
        },
        u'web.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'distance': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'last_updated_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'null': 'True', 'to': u"orm['web.UserProfile']"}),
            'location': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'organizations': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'members'", 'symmetrical': 'False', 'through': u"orm['web.ProfileOrganization']", 'to': u"orm['web.Organization']"}),
            'story': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'profile'", 'unique': 'True', 'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['web']