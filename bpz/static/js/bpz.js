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

jQuery(document).ready(function () {
  L.mapbox.accessToken ='pk.eyJ1IjoiamR1bmdhbiIsImEiOiJlOTl6MFpNIn0.-3o5vIOCjkfXd-7ibZrb8A'
  map = L.mapbox.map('map-canvas', 'jdungan.jbbebonl').setView([36.1587336,-95.9940543],16);
    
});
