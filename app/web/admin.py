
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

from django.contrib import admin
from django.contrib.contenttypes import generic

from leaflet.admin import LeafletGeoAdmin

from web.models import (Image, Location, Organization, Pet, Transport,
    TransportSegment, UserProfile, )


class UserProfileAdmin(LeafletGeoAdmin):
    """
    The admin interface for UserProfiles.
    """

admin.site.register(UserProfile, UserProfileAdmin)


class PetImageInline(generic.GenericTabularInline):
    model = Image
    exclude = ('width', 'height', 'size', 'source_url', )

class PetAdmin(admin.ModelAdmin):
    """
    The admin interface for Pets.
    """
    inlines = [PetImageInline,]
    exclude = ('images', )

admin.site.register(Pet, PetAdmin)


class TransportSegmentInline(admin.TabularInline):
    model = TransportSegment
    fk_name = 'transport'

class TransportAdmin(admin.ModelAdmin):
    """
    The admin interface for Transports.
    """
    inlines = [
        TransportSegmentInline,
    ]

    readonly_fields = ('tracking_number', )
    fieldsets = (
        (None, {
            'fields': ('tracking_number', 'shipper', 'receiver', 'notes',)
        }),

        ('Status', {
            'fields': ('status', 'started_on', 'finished_on')
        }),

        ('History', {
            'fields' : ('created_by', 'last_updated_by',  )
        }),

    )
admin.site.register(Transport, TransportAdmin)


class TransportSegmentAdmin(LeafletGeoAdmin):
    """
    The admin interface for TransportSegments.
    """

admin.site.register(TransportSegment, TransportSegmentAdmin)


class OrganizationAdmin(admin.ModelAdmin):
    """
    The admin interface for Organizations.
    """

admin.site.register(Organization, OrganizationAdmin)



class LocationAdmin(LeafletGeoAdmin):
    """
    The admin interface for Locations.
    """

admin.site.register(Location, LocationAdmin)
