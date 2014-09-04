var call_map, bpz, value, _fn, _i, _len;


function Location() {
  var options = {
    enableHighAccuracy: true
  },
    inner_pos = {},
    dfd = new $.Deferred(),
    moved = function(pos) {
      inner_pos = pos || {};
      dfd.resolve(this)
    },
    fail = function(err) {
      if (err) {
        console.warn('ERROR(' + err.code + '): ' + err.message);
      }
      dfd.reject()
    };

  this.__defineGetter__("lat", function() {
    return inner_pos.coords ? inner_pos.coords.latitude : null;
  });

  this.__defineGetter__("lng", function() {
    return inner_pos.coords ? inner_pos.coords.longitude : null;
  });

  this.__defineGetter__("pos", function() {
      return {lng:this.lng,lat:this.lat};
    });

  this.WatchID = navigator.geolocation.watchPosition(moved, fail, options);

  this.ready = dfd.promise()
}



bpz = {
  _map:false,
  api: {},
  'location': new Location()
};

bpz.__defineGetter__("map", function() {
  if (!bpz._map){
    L.mapbox.accessToken ='pk.eyJ1IjoiamR1bmdhbiIsImEiOiJlOTl6MFpNIn0.-3o5vIOCjkfXd-7ibZrb8A'
    bpz._map=L.mapbox.map('map-canvas', 'jdungan.jbbebonl').setView([36.1587336,-95.9940543],12); 
  }
  return bpz._map
});


bpz.api.raw = function(resource, ajax_params) {
  ajax_params = ajax_params || {};
  return $.ajax({
    type: "get",
    url: "/api" + resource,
    data: ajax_params,
    dataType: "json"
  });
};

call_map = [["cases", "/cases"],["hoa", "/hoas"]];

_fn = function(value) {
  return bpz.api[value[0]] = function(params) {
    return bpz.api.raw(value[1], params);
  };
};

for (_i = 0, _len = call_map.length; _i < _len; _i++) {
  value = call_map[_i];
  _fn(value);
}

