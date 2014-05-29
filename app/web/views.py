
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


from django.shortcuts import render, get_object_or_404

from web.models import (Transport, )

def index(request):
    transport_list = Transport.objects.all().values('tracking_number',
        'manifest__images__image', 'manifest__name')
    return render(request, 'pawtrain/index.html',
         { 'transport_list': transport_list, }
    )

def account_profile(request):
    return render(request, 'pawtrain/account_profile.html')

def dashboard(request):
    return render(request, 'pawtrain/dashboard.html')

def transport_detail(request, tracking_number):
    transport = get_object_or_404(Transport, tracking_number=tracking_number)
    return render(request, 'pawtrain/transport_detail.html', {
        'transport': transport
    })
