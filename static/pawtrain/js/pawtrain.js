/*

  =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

  PAWTRAIN

      Pet underground railroad

  Authors: Baron L. Chandler, baron@venturecranial.com
  -----------------------------------------------------------------------
  COPYRIGHT ©2014 Venture Cranial, LLC
  =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

*/

define([
    'jquery',
    'underscore',
    'leaflet',
    'bootstrap',
    'leaflet-control-geocoder',
    'leaflet-routing-machine',
], function($, _, L) {

    var didLaunch = function() {

        console.log('did launch');
        console.log('L is ', L);


        var pawtrain_signout = $('#pawtrain-signout');

        /*
          If user clicks sign out link, and then hits sign out
          button, the data for signout will be true and we submit
          the form which POSTs the signout.
        */
        pawtrain_signout.on('hidden.bs.modal', function (e) {
            if (pawtrain_signout.data('signout') === 'true') {
                $('form[name="logout-form"]').submit();
            }
        });

    };

    return {
      didLaunch: didLaunch
    };
});
