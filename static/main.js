/*

  =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

  PAWTRAIN

      Pet underground railroad

  Authors: Baron L. Chandler, baron@venturecranial.com
  -----------------------------------------------------------------------
  COPYRIGHT ©2014 Venture Cranial, LLC
  =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

*/

require.config( {

    baseUrl: '/static',

    paths: {

        'jquery':               'jquery/1.11.1/jquery-1.11.1.min',
        'underscore':           'underscore/1.6.0/underscore-min',

        'moment':               'moment/2.6.0/moment.min',

        'bootstrap':            'bootstrap/js/bootstrap.min',

        'leaflet':              'leaflet/0.7.3/leaflet',

        'leaflet-routing-machine': 'leaflet-routing-machine/0.2.1/js/leaflet-routing-machine.min',
        'leaflet-control-geocoder': 'leaflet-control-geocoder/0.2.1/js/Control.Geocoder',

        'pawtrain':             'pawtrain/js/pawtrain'
    },

    shim: {
        'bootstrap': {
            deps: ['jquery'],
            exports: '$.fn.modal'
        },
        'underscore': {
            deps: [],
            exports: '_'
        },
        'jquery' : {
            exports: 'jQuery'
        },
        'moment': {
            exports: 'moment'
        },
        'leaflet-routing-machine': {
            deps: ['leaflet', 'leaflet-control-geocoder'],
        },
        'leaflet-control-geocoder': {
            deps: ['leaflet'],
        },
        'leaflet': {
            exports: 'L',
        }

    }
});


require([
    'pawtrain'
    ], function(pawtrain) {
        pawtrain.didLaunch();
    }
);
