// Google Maps JavaScript SDK
function initialize() {
  var mapOptions = {
    center: new google.maps.LatLng(36.1314, -95.9372),
    zoom: 8
  };
  var map = new google.maps.Map(document.getElementById("map-canvas"), mapOptions);
}
google.maps.event.addDomListener(window, 'load', initialize);

// Location
$(document).ready(function() {
  getLocation();
});

function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(processLocation);
  }
}

function processLocation(position) {
  var latitude = position.coords.latitude;
  var longitude = position.coords.longitude;
  window.location = '#latitude=' + latitude + '&longitude=' + longitude;
}
