
# -*- coding: utf-8 -*-
#
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#
# PAWTRAIN
#
#     Pet underground railroad
#
#
# Authors: Baron L. Chandler, baron@venturecranial.com
# -----------------------------------------------------------------------
# COPYRIGHT ©2014 Venture Cranial, LLC
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#


import hashlib
import struct

from django.contrib.gis.db import models

from datetime import datetime
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType

from web.constants import (JOURNAL_ENTRY_CHOICES,
                           JOURNAL_ENTRY_TEXT_TYPE,
                           TRANSPORT_STATUS_CHOICES,
                           TRANSPORT_STATUS_NEW,
                           GENDER_CHOICES,
                           GENDER_FEMALE,
                           TRANSPORT_ROLE_CHOICES,
                           TRANSPORT_ROLE_GENERAL,
                           SEGMENT_STATUS_CHOICES,
                           SEGMENT_STATUS_ONTIME,
                           FEEDBACK_CHOICES,
                           PET_TYPE_CHOICES,
                           ATTRIBUTE_CHOICES,
                           SEGMENT_ROLE_CHOICES, )

from web.util import base36encode

class Feedback(models.Model):

    """
    Feedback left about a person, shipment, or other item.
    """

    content_type = models.ForeignKey(ContentType, null=True)
    object_id = models.PositiveIntegerField(null=True)
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    kind = models.CharField(max_length=4, choices=FEEDBACK_CHOICES)
    weight = models.IntegerField()
    notes = models.CharField(max_length=512, blank=True )
    posted = models.DateTimeField(auto_now_add=True)
    posted_by = models.ForeignKey('UserProfile', related_name='feedbacks_posted')

    def __unicode__(self):
        return '"%s"\n    -- %s, %s' % (
            self.notes,
            self.posted_by.full_name,
            self.posted.strftime('%m %d %Y %I:%M %p')
        )


class Image(models.Model):
    """
        Images in PawTrain
    """
    posted = models.DateTimeField(auto_now=True)
    posted_by = models.ForeignKey('UserProfile', related_name='posted_images')
    image = models.ImageField(upload_to='images',
        width_field='width', height_field='height')
    source_url = models.CharField(max_length=255, null=True, blank=True)
    width = models.IntegerField(null=True, blank=True, default=0)
    height = models.IntegerField(null=True, blank=True, default=0)
    size = models.IntegerField(null=True, blank=True, default=0)
    feedback = generic.GenericRelation(Feedback,
      content_type_field='content_type', object_id_field='object_id')

    content_type = models.ForeignKey(ContentType, null=True)
    object_id = models.PositiveIntegerField(null=True)
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    def __unicode__(self):
        return u'%d x %d, %d bytes' % (self.width, self.height, self.size)


class UserProfile(models.Model):
    """
        A profile for a user in PawTrain
    """

    user = models.OneToOneField('auth.User', related_name='profile')
    organizations = models.ManyToManyField('Organization',
        through='ProfileOrganization', related_name='members',
        help_text='User is a member of these rescue organizations.')
    images = generic.GenericRelation(Image,
      content_type_field='content_type', object_id_field='object_id')
    feedback = generic.GenericRelation(Feedback,
        content_type_field='content_type', object_id_field='object_id')
    story = models.CharField(max_length=512, null=True, blank=True,
        help_text='Biographical story about this user.')

    last_updated = models.DateTimeField(auto_now=True)
    last_updated_by = models.ForeignKey('UserProfile', related_name='+',
        editable=False, null=True)
    location = models.PointField()
    distance = models.FloatField()

    objects = models.GeoManager()

    @property
    def full_name(self):
        return self.user.first_name + ' ' + self.user.last_name

    def __unicode__(self):
        return self.full_name + ' (' + self.user.username + ')'


class ProfileOrganization(models.Model):
    """
        Describes a user's relationship to an organization.
    """
    user = models.ForeignKey('UserProfile')
    organization = models.ForeignKey('Organization')
    role =  models.CharField(max_length=64)

    last_updated = models.DateTimeField(auto_now=True)


class Organization(models.Model):
    """
        An organization.
    """
    name = models.CharField(max_length=64)
    logo = models.OneToOneField('Image', null=True, blank=True)
    description = models.CharField(max_length=512)
    created_on = models.DateTimeField(auto_now_add=True)
    feedback = generic.GenericRelation(Feedback,
       content_type_field='content_type', object_id_field='object_id')
    last_updated = models.DateTimeField(auto_now=True)
    last_updated_by = models.ForeignKey('UserProfile',
        related_name='+', editable=False, null=True)

    def __unicode__(self):
        return self.name


class Pet(models.Model):
    """
        An individual package that is shipped and received.
    """
    pet_type = models.CharField(max_length=32, choices=PET_TYPE_CHOICES,
        null = False)
    name =  models.CharField(max_length=64)

    location = models.ForeignKey('Location',
        related_name='pets_located_here', null=True, blank=True)
    story = models.CharField(max_length=512)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    last_updated_by = models.ForeignKey('UserProfile',
        related_name='+', editable=False, null=True)
    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    created_by = models.ForeignKey('UserProfile',
        related_name='+', editable=False, null=True)
    thumbnail = models.ForeignKey('Image',
        related_name='+', null=True, blank=True)
    images = generic.GenericRelation(Image,
      content_type_field='content_type', object_id_field='object_id')
    rescued_by = models.ForeignKey('Organization', null=True,
        blank=True, related_name='rescued_pets')

    transport = models.ForeignKey('Transport', null=True, blank=True,
        related_name='manifest')


    def __unicode__(self):
        return self.name

    def key(self):
        return self.pk

    def attributes_as_dict(self):
        return dict(self.petattribute_set.values_list(
                    'attribute__attribute', 'value'))


class PetAttribute(models.Model):
    pet = models.ForeignKey('Pet')
    attribute = models.ForeignKey('Attribute')
    value = models.CharField(max_length=255, blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True)
    last_updated_by = models.ForeignKey('UserProfile', related_name='+')

    def __unicode__(self):
        return '%s/%s: %s' % (self.pet.name, self.attribute.attribute,
            self.value, )


class Attribute(models.Model):
    kind = models.CharField(max_length=4, choices=ATTRIBUTE_CHOICES)
    pets = models.ManyToManyField('Pet', through='PetAttribute')

    attribute = models.CharField(max_length=64)
    display_name = models.CharField(max_length=128)
    description = models.CharField(max_length=512)
    special_choices = models.CharField(max_length=64, blank=True,
        null=True)
    special_validation = models.CharField(max_length=64, blank=True,
        null=True)
    last_updated = models.DateTimeField(auto_now=True)
    last_updated_by = models.ForeignKey('UserProfile', related_name='+')

    def __unicode__(self):
        return '%s (%s)' % (self.display_name, self.attribute)


class Location(models.Model):
    name = models.CharField(max_length=128)
    address = models.CharField(max_length=128, blank=True, null=True)
    geo = models.PointField()
    description = models.CharField(max_length=256, blank=True, null=True)
    feedback = generic.GenericRelation(Feedback,
        content_type_field='content_type', object_id_field='object_id')

    def __unicode__(self):
      try:
        return '%s (%f, %f)' % (self.name, self.geo.coords[0], self.geo.coords[1])
      except:
        return self.name


class SegmentRoles(models.Model):
    """
        Relates a user to a segment by giving them a role.
    """
    segment = models.OneToOneField('TransportSegment',
        related_name='volunteers')
    user = models.ManyToManyField('UserProfile', related_name='+')
    role = models.CharField(max_length=4, choices=TRANSPORT_ROLE_CHOICES)
    priority = models.IntegerField()
    status = models.CharField(max_length=4, choices=SEGMENT_ROLE_CHOICES)


class TransportSegment(models.Model):
    sequence = models.IntegerField()
    pick_up_location = models.ForeignKey('Location',
        related_name='pickup+')
    drop_off_location = models.ForeignKey('Location',
        related_name='dropoff+')
    pick_up_datetime = models.DateTimeField()
    drop_off_datetime = models.DateTimeField()
    duration = models.TimeField()
    miles = models.IntegerField()

    transport = models.ForeignKey('Transport', related_name='segments',
        null=True, blank=True)

    status = models.CharField(max_length=4,
        choices=SEGMENT_STATUS_CHOICES, default=SEGMENT_STATUS_ONTIME)
    offset = models.TimeField(blank=True, null=True)
    notes = models.CharField(max_length=512, blank=True, null=True)
    feedback = generic.GenericRelation(Feedback,
        content_type_field='content_type', object_id_field='object_id')
    last_updated = models.DateTimeField(auto_now=True)
    last_updated_by = models.ForeignKey('UserProfile', related_name='+')

    def __unicode__(self):
        return '%s - %s to %s (%d miles)' % (self.transport.tracking_number,
          self.pick_up_location.name, self.drop_off_location.name,
          self.miles, )

class Transport(models.Model):
    """
        Represents a shipment.
    """
    shipper = models.ForeignKey('UserProfile',
        related_name='packages_shipped')
    receiver = models.ForeignKey('UserProfile',
        related_name='packages_received')
    tracking_number = models.CharField(max_length=30, unique=True,
      default=lambda: Transport.generate_tracking_number())
    notes = models.CharField(max_length=512, blank=True, null=True)

    history = generic.GenericRelation('Feedback',
        content_type_field='content_type', object_id_field='object_id')

    status = models.CharField(max_length=4,
        choices=TRANSPORT_STATUS_CHOICES, default=TRANSPORT_STATUS_NEW)
    started_on = models.DateTimeField(blank=True, null=True)
    start_location = models.ForeignKey('Location',
        related_name='start_location+', null=True, )

    finished_on = models.DateTimeField(blank=True, null=True)
    finish_location = models.ForeignKey('Location',
        related_name='finish_location+', null=True, )

    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('UserProfile', related_name='+')
    last_updated = models.DateTimeField(auto_now=True)
    last_updated_by = models.ForeignKey('UserProfile', related_name='+')

    def __unicode__(self):
        try:
          count = self.segments.count()
          return '%s - %d segments from %s to %s' % (self.tracking_number,
              count, self.start_location.name, self.finish_location.name, )
        except:
            return 'Transport %s' % (self.tracking_number, )

    def save(self, *args, **kwargs):

          # If there are segments, update start and finish locations

          if self.segments.count() > 0:
              segments = self.segments.all().order_by('sequence')
              self.start_location = segments.first().pick_up_location
              self.finish_location = segments.last().drop_off_location

          super(Transport, self).save(*args, **kwargs)

    @staticmethod
    def generate_tracking_number():
        tm = datetime.utcnow().__str__()
        (a, b) = struct.unpack('ll', hashlib.md5(tm).digest())
        return "PT" + base36encode(abs(a+b)).zfill(13)


class TransportLogEntry(models.Model):
    """
        Simple text or image journal/discussion board which can track the
        progress of the shipment.
    """
    shipment = models.ForeignKey('Transport', related_name='log_entries')
    timestamp = models.DateTimeField()
    image = models.OneToOneField('Image', null=True, blank=True)
    text = models.CharField(max_length=512, null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)
    last_updated_by = models.ForeignKey('UserProfile',
        related_name='+', editable=False)
