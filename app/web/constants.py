#
# coding=UTF-8
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


PET_TYPE_DOG = 'canine'
PET_TYPE_CAT = 'feline'

PET_TYPE_CHOICES = (
    (PET_TYPE_DOG, 'Dog'),
    (PET_TYPE_CAT, 'Cat'),
)


GENDER_FEMALE = 'F'
GENDER_MALE = 'M'
GENDER_NA = 'N'
GENDER_UNKNOWN = 'U'

GENDER_CHOICES = (
    (GENDER_FEMALE, 'Female'),
    (GENDER_MALE, 'Male'),
    (GENDER_NA, 'Not Applicable'),
    (GENDER_UNKNOWN, 'Unknown'),
)


JOURNAL_ENTRY_TEXT_TYPE = 'TXT'
JOURNAL_ENTRY_IMAGE_TYPE = 'IMG'

JOURNAL_ENTRY_CHOICES = (
    (JOURNAL_ENTRY_TEXT_TYPE, 'Text log'),
    (JOURNAL_ENTRY_IMAGE_TYPE, 'Image'),
)


TRANSPORT_ROLE_GENERAL = 'GEN'
TRANSPORT_ROLE_MEDICAL = 'MED'
TRANSPORT_ROLE_FAMILY = 'FAM'
TRANSPORT_ROLE_SHIPPER = 'SHP'
TRANSPORT_ROLE_RECEIVER = 'RCV'
TRANSPORT_ROLE_DRIVER = 'DRV'
TRANSPORT_ROLE_COORDINATOR = 'CRD'
TRANSPORT_ROLE_SCHEDULER = 'SCH'
TRANSPORT_ROLE_PRIMARY = 'PRI'
TRANSPORT_ROLE_SECONDARY = 'SEC'

TRANSPORT_ROLE_CHOICES = (
    (TRANSPORT_ROLE_SHIPPER, 'Shipper'),
    (TRANSPORT_ROLE_RECEIVER, 'Receiver'),
    (TRANSPORT_ROLE_DRIVER, 'Segment Driver'),
    (TRANSPORT_ROLE_FAMILY, 'Family Member'),
    (TRANSPORT_ROLE_MEDICAL, 'Medical Contact'),
    (TRANSPORT_ROLE_COORDINATOR, 'Coordinator'),
    (TRANSPORT_ROLE_SCHEDULER, 'Scheduler'),
    (TRANSPORT_ROLE_GENERAL, 'General'),
    (TRANSPORT_ROLE_PRIMARY, 'Primary'),
    (TRANSPORT_ROLE_SECONDARY, 'Secondary'),
)


CONTACT_METHOD_PHONE = 'PHON'
CONTACT_METHOD_CELL = 'CELL'
CONTACT_METHOD_EMAIL = 'EML'
CONTACT_METHOD_OTHER = 'OTHR'

CONTACT_METHOD_CHOICES = (
    (CONTACT_METHOD_PHONE, 'Phone'),
    (CONTACT_METHOD_CELL, 'Cell Phone'),
    (CONTACT_METHOD_EMAIL, 'Email'),
    (CONTACT_METHOD_OTHER, 'Other (see notes)'),
)


TRANSPORT_STATUS_NEW = 'NEW'
TRANSPORT_STATUS_FILLING = 'FLNG'
TRANSPORT_STATUS_FILLED = 'FILD'
TRANSPORT_STATUS_SCHEDULED = 'SCHD'
TRANSPORT_STATUS_RUNNING = 'RUN'
TRANSPORT_STATUS_DELIVERED = 'DLVR'
TRANSPORT_STATUS_CANCELED = 'CNCL'
TRANSPORT_STATUS_ONHOLD = 'HELD'

TRANSPORT_STATUS_CHOICES = (
    (TRANSPORT_STATUS_NEW, 'New Transport'),
    (TRANSPORT_STATUS_FILLING, 'Currently Filling'),
    (TRANSPORT_STATUS_FILLED, 'Filled'),
    (TRANSPORT_STATUS_SCHEDULED, 'Scheduled'),
    (TRANSPORT_STATUS_RUNNING, 'In Progress'),
    (TRANSPORT_STATUS_DELIVERED, 'Delivered'),
    (TRANSPORT_STATUS_CANCELED, 'Canceled'),
    (TRANSPORT_STATUS_ONHOLD, 'On Hold'),
)


SEGMENT_STATUS_PENDING = 'PEND'
SEGMENT_STATUS_REQUESTED = 'REQ'
SEGMENT_STATUS_APPROVED = 'APRV'
SEGMENT_STATUS_ONTIME = 'ONTM'
SEGMENT_STATUS_EARLY_ARRIVAL = 'EARR'
SEGMENT_STATUS_LATE_ARRIVAL = 'LARR'
SEGMENT_STATUS_EARLY_DEPARTURE = 'EDEP'
SEGMENT_STATUS_LATE_DEPARTURE = 'LDEP'
SEGMENT_STATUS_NOSHOW_DROPOFF = 'NSDO'
SEGMENT_STATUS_NOSHOW_PICKUP = 'NSPU'

SEGMENT_STATUS_CHOICES = (
    (SEGMENT_STATUS_REQUESTED, 'Requested'),
    (SEGMENT_STATUS_PENDING, 'Pending Approval'),
    (SEGMENT_STATUS_APPROVED, 'Approved'),
    (SEGMENT_STATUS_ONTIME, 'On schedule'),
    (SEGMENT_STATUS_EARLY_ARRIVAL, 'Arriving earlier than scheduled'),
    (SEGMENT_STATUS_LATE_ARRIVAL, 'Arriving later than scheduled'),
    (SEGMENT_STATUS_EARLY_DEPARTURE, 'Leaving earlier than scheduled'),
    (SEGMENT_STATUS_LATE_DEPARTURE, 'Leaving later than scheduled'),
    (SEGMENT_STATUS_NOSHOW_DROPOFF, 'No-Show - Drop off'),
    (SEGMENT_STATUS_NOSHOW_PICKUP, 'No-Show - Pick-up'),
)


SEGMENT_ROLE_CONFIRMED = 'CNF'
SEGMENT_ROLE_REQUESTED = 'REQ'
SEGMENT_ROLE_CHOICES = (
    (SEGMENT_ROLE_CONFIRMED, 'Confirmed'),
    (SEGMENT_ROLE_REQUESTED, 'Requested'),
    )



ATTRIBUTE_PHYSICAL = 'PHY'
ATTRIBUTE_PSYCHOLOGICAL = 'PSY'
ATTRIBUTE_HEALTH = 'HLT'
ATTRIBUTE_BEHAVIORAL = 'BEH'
ATTRIBUTE_CHOICES = (
    (ATTRIBUTE_PHYSICAL, 'Physical'),
    (ATTRIBUTE_PSYCHOLOGICAL, 'Psychological'),
    (ATTRIBUTE_HEALTH, 'Health'),
    (ATTRIBUTE_BEHAVIORAL, 'Behavioral'),
)

FEEDBACK_NEGATIVE = '-1'
FEEDBACK_POSITIVE = '+1'

FEEDBACK_CHOICES = (
    (FEEDBACK_POSITIVE, 'Positive Feedback'),
    (FEEDBACK_NEGATIVE, 'Negative Feedback'),
)


PACKAGE_TYPE_DOG = 'DOG'
PACKAGE_TYPE_OTHER = 'OTHER'

PACKAGE_TYPE_CHOICES = (
    (PACKAGE_TYPE_DOG, 'Dog'),
    (PACKAGE_TYPE_OTHER, 'Other'),
)
