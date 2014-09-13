
function Location() {
  var  dfd = new $.Deferred(),
    _pos ={},
    _onMove = function (pos) {},
    options = {
      enableHighAccuracy: true
    },
    fail = function(err) {
      if (err) {
        console.warn('ERROR(' + err.code + '): ' + err.message);
      }
      dfd.reject(err)
    };
  
  this.on ={}

  Object.defineProperty(this, "lat", {
    get: function() {return _pos.coords ? _pos.coords.latitude : null; }
  })

  Object.defineProperty(this, "lng", {
    get: function() {return _pos.coords ? _pos.coords.longitude : null; }
  })

  Object.defineProperty(this, "pos", {
    get: function() {
      return { lng: _pos.coords.longitude, lat: _pos.coords.latitude}; 
    },
    set: function(new_pos){ 
      _pos = new_pos
      if (_onMove){
        _onMove(pos_desc.get())
      }
      dfd.resolve(this)
    }
  })
  
  this.on.move = function(fn) {
     _onMove = fn; 
  }

  pos_desc = Object.getOwnPropertyDescriptor(this, 'pos');

  WatchID = navigator.geolocation.watchPosition(pos_desc.set, fail, options);

  this.ready = dfd.promise()

}

//TODO: Move access token into environment variable 
L.mapbox.accessToken ='pk.eyJ1IjoiamR1bmdhbiIsImEiOiJlOTl6MFpNIn0.-3o5vIOCjkfXd-7ibZrb8A'

var bpz = {
  _map:false,
  api: {},
  'location': new Location(),
  get map() {
    if (!bpz._map){
      bpz._map=L.mapbox.map('map-canvas', 'jdungan.jbbebonl').setView([36.1587336,-95.9940543],12); 
    }
    return bpz._map
  },
  stored:{
    get currentLatLng(){
      return  JSON.parse(sessionStorage.getItem("latlng"));
    },
    set currentLatLng(new_latlng){
      sessionStorage.setItem("latlng",JSON.stringify(new_latlng));
    },
    get streetAddress(){
      return  JSON.parse(sessionStorage.getItem("streetAddress"));
    },
    set streetAddress(address){
      sessionStorage.setItem("streetAddress",JSON.stringify(address));
    }
  },
  updateMap : function (data) {
    bpz.map.featureLayer.setGeoJSON(data);
    bpz.map.featureLayer.on('click',function (e) {
      var container = $('body,html'),
          scrollTo = $('#object_id-'+e.layer.feature.properties.object_id);
      container.animate({
          scrollTop: scrollTo.offset().top - container.offset().top -325
      })
      bpz.layers.zoom(e.layer);
    })
  },
  updatePosition: function (new_latlng) {
     bpz.map.setView(new_latlng);
     bpz.map.setZoom(14);
  },
  activateMap: function () {
    var cL = bpz.stored.currentLatLng;
    d3.select("#map-canvas").classed("active",true);
    if (cL){
       bpz.updatePosition(cL);
    } else {
      bpz.location.ready
        .done(function () {
          bpz.stored.currentLatLng=bpz.location.pos;
          bpz.updatePosition(bpz.location.pos);
        })
        .fail(function (err) {
          if (err.code===1){
            $(".ask").removeClass("hidden");
          } 
        });
    }
  },
  layers: {
    zoom: function (layer) {
             bpz.map.fitBounds(layer.getBounds(),{maxZoom:16,animate:true});
          }
  },
  lists:{
    build: function (selector,data) {
      var ul = d3.select(selector)
      //ul.style({position:'relative',top:'300px'})
      
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
          });

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
                  var bb=this.getBBox(),
                  scale = (40/Math.max(bb.height,bb.width)),
                  tx = -bb.x*scale,
                  ty = -bb.y*scale;
                  return "translate("+tx+","+ty+") scale("+scale+")";
                },
              });
    },
    append:{
      hoa: function (selector) {
          li = d3.selectAll(selector+" li div.media");
          li  
            .insert("div")
              .classed("media-body",true)
              .attr({id: function (d,i) {
                return "object_id-"+d.properties.object_id;
              },})
              .append("p").text(function (d) {
                return "NEIGHBORHOOD: "+d.properties.name;
              })
              .append("p").text(function (d) {
                return "ASSOCIATION: "+d.properties.hoa_name;
              })
      },
      cases: function (selector) {
        li = d3.selectAll(selector+" li div.media")
        li
          .insert("div")
            .classed("media-body",true)
            .attr({id: function (d,i) {
              return "object_id-"+d.properties.object_id;
            },})
            .append("p").text(function (d) {
              return "STATUS: "+d.properties.status; 
            })
            .append("p").text(function (d) {
              return "CASE TYPE: "+d.properties.case_type; 
            })
            .append("p").text(function (d) {
              return "HEARING DATE: "+d.properties.hearing_date;
            })
            .append("p").text(function (d) {
              return "LOCATION: "+d.properties.location;
            })
            .append("p").text("APPLICATION: ")
            .append("a").text(function (d) {
              return d.properties.case_id;
            })
            .attr({
              target:"_blank",
              href: function (d) {
              return d.properties.link;
              },
            })
      }
    }
    
  }
};

//self executing to append api without junking up global namespace
(function (api) {
  var value, _fn, _i, _len,
  call_map = [["cases", "/cases"],["hoa", "/hoas"]],
  call = function(resource, ajax_params) {
    ajax_params = ajax_params || {};
    return $.ajax({
      type: "get",
      url: "/api" + resource,
      data: ajax_params,
      dataType: "json"
    });
  };

  _fn = function(value) {
    return api[value[0]] = function(params) {
      return call(value[1], params);
    };
  };

  for (_i = 0, _len = call_map.length; _i < _len; _i++) {
    value = call_map[_i];
    _fn(value);
  }
})(bpz.api)

