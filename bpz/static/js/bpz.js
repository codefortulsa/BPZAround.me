// function Location() {
//   var options = {
//     enableHighAccuracy: true
//   },
//     inner_pos = {},
//     dfd = new $.Deferred(),
//     moved = function(pos) {
//       inner_pos = pos || {};
//       dfd.resolve()
//     },
//     fail = function(err) {
//       if (err) {
//         console.warn('ERROR(' + err.code + '): ' + err.message);
//       }
//       dfd.reject()
//     };
//
//   this.__defineGetter__("lat", function() {
//     return inner_pos.coords ? inner_pos.coords.latitude : null;
//   });
//
//   this.__defineGetter__("lng", function() {
//     return inner_pos.coords ? inner_pos.coords.longitude : null;
//   });
//
//   this.WatchID = navigator.geolocation.watchPosition(moved, fail, options);
//
//   this.ready = dfd.promise()
// }
//
//
//


var call_map, bpz, value, _fn, _i, _len;

bpz = {
  api: {}
};


bpz.api.raw = function(resource, ajax_params) {
  ajax_params = ajax_params || {};
  return $.ajax({
    type: "get",
    url: "/api" + resource,
    data: ajax_params,
    dataType: "json"
  });
};

call_map = [["cases", "/cases"]];

_fn = function(value) {
  return bpz.api[value[0]] = function(params) {
    return bpz.api.raw(value[1], params);
  };
};

for (_i = 0, _len = call_map.length; _i < _len; _i++) {
  value = call_map[_i];
  _fn(value);
}



document.dispatchEvent(new Event('bpz_load'))

jQuery(document).ready(function () {

  L.mapbox.accessToken ='pk.eyJ1IjoiamR1bmdhbiIsImEiOiJlOTl6MFpNIn0.-3o5vIOCjkfXd-7ibZrb8A'
  map = L.mapbox.map('map-canvas', 'jdungan.jbbebonl').setView([36.1587336,-95.9940543],16);
  $(window).trigger('bpz_load');
    
});
