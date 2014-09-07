var call_map, bpz, value, _fn, _i, _len;



//TODO: replace 
function Location() {
  var options = {
    enableHighAccuracy: true
  },
    dfd = new $.Deferred(),
    inner_pos = {}
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
    return {
      lng: this.lng,
      lat: this.lat
    };
  });
  this.position = inner_pos;

  this.WatchID = navigator.geolocation.watchPosition(moved, fail, options);

  this.ready = dfd.promise()

}



bpz = {
  _map:false,
  api: {},
  'location': new Location(),
  get map() {
    if (!bpz._map){
      //TODO: Move access token into environment variable 
      L.mapbox.accessToken ='pk.eyJ1IjoiamR1bmdhbiIsImEiOiJlOTl6MFpNIn0.-3o5vIOCjkfXd-7ibZrb8A'
      bpz._map=L.mapbox.map('map-canvas', 'jdungan.jbbebonl').setView([36.1587336,-95.9940543],12); 
    }
    return bpz._map
  },
  updateMap : function (data) {
    bpz.map.featureLayer.setGeoJSON(data);

    bpz.map.featureLayer.on('click',function (e) {

      var container = $('body,html'),
          scrollTo = $('#object_id-'+e.layer.feature.properties.object_id);

      container.animate({
          scrollTop: scrollTo.offset().top - container.offset().top -325
      })

      bpz.layers.zoom(e.layer)

    })

  },
  activateMap: function () {
    d3.select("#map-canvas").classed("active",true)
    bpz.location.ready.done(function (d) {
      bpz.map.setView(bpz.location.pos,16)  

    })
  },
  layers: {
    zoom: function (layer) {
             bpz.map.fitBounds(layer.getBounds(),{maxZoom:16,animate:true})
          }
  },
  lists:{
    build: function (selector,data) {
      var ul = d3.select(selector)
      ul.style({position:'relative',top:'300px'})
      
      //create an li for all features
      li = ul.selectAll("li")
        .data(data.features)
        .enter()
        .append("li")
          .classed("list-group-item",true)
        .append("div")
          .classed("media",true)
          .on("click",function (d,i) {
            var obj_id = d.properties.object_id
            layers = bpz.map.featureLayer.getLayers()
            _.each(layers,function (element) {
              if (element.feature.properties.object_id === obj_id){
                bpz.layers.zoom(element)    
              }
            })
          })

      // add a thumbnail of the feature 
      li
        .append("div")
        .classed("pull-left",true)
        .insert("svg")
          .classed("media-object",true)
          .attr({width:50,height:50})
          .insert("path")
              .attr({
                d: d3.geo.path(),
                class: "leaflet-clickable",
                transform: function (d,i,e) {
                  bb=this.getBBox()
                  scale = (40/Math.max(bb.height,bb.width))
                  tx = -bb.x*scale
                  ty = -bb.y*scale
                  return "translate("+tx+","+ty+") scale("+scale+")"
                },

              })
      
    },
    append:{
      hoa: function (selector) {
          li = d3.selectAll(selector+" li div.media")
          li  
            .insert("div")
              .classed("media-body",true)
              .attr({id: function (d,i) {
                return "object_id-"+d.properties.object_id
              },})
              .append("p").text(function (d) {
                return "NEIGHBORHOOD: "+d.properties.name
              })
              .append("p").text(function (d) {
                return "ASSOCIATION: "+d.properties.hoa_name
              })
      },
      cases: function (selector) {
        li = d3.selectAll(selector+" li div.media")
        li
          .insert("div")
            .classed("media-body",true)
            .attr({id: function (d,i) {
              return "object_id-"+d.properties.object_id
            },})
            .append("p").text(function (d) {
              return "STATUS: "+d.properties.status 
            })
            .append("p").text(function (d) {
              return "CASE TYPE: "+d.properties.case_type 
            })
            .append("p").text(function (d) {
              return "HEARING DATE: "+d.properties.hearing_date 
            })
            .append("p").text(function (d) {
              return "LOCATION: "+d.properties.location 
            })
            .append("p").text("APPLICATION: ")
            .append("a").text(function (d) {
              return d.properties.case_id 
            })
            .attr({
              target:"_blank",
              href: function (d) {
              return d.properties.link
              },
            })
      }
    }
    
  }
};

bpz.api.call = function(resource, ajax_params) {
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
    return bpz.api.call(value[1], params);
  };
};

for (_i = 0, _len = call_map.length; _i < _len; _i++) {
  value = call_map[_i];
  _fn(value);
}

