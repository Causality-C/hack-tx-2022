// need to do something about this
mapboxgl.accessToken = 'pk.eyJ1IjoiZ2VvcmdlazcyMiIsImEiOiJjbDlhaG05aG0waGJjM3hxd29sNmV1bnUwIn0.5BQvW7-_lTlIbS36AjRs7g';


class Map {

    constructor(containerName, lat, long, callback){
        this.map = new mapboxgl.Map({
            container: containerName, // container id
            // Choose from Mapbox's core styles, or make your own style with Mapbox Studio
            style: 'mapbox://styles/mapbox/streets-v11',
            center: [long, lat], // starting position
            zoom: 17 // starting zoom
        });

        // Create a marker and add it to the map.
        this.marker = new mapboxgl.Marker().setLngLat([long, lat]).setDraggable(true).addTo(this.map);

        this.marker.on('dragend', (e) => {
            const lngLat = this.marker.getLngLat()
            callback(lngLat['lng'], lngLat['lat']);
        });

    }

    updateMap(long, lat){
        this.map.setCenter([long, lat]);
        this.marker.setLngLat([long, lat]);
    }

}

// testing

m = new Map("map", 30.288405404040404, -97.73681904040404, (x, y) => console.log(x + " " + y))

setTimeout(() => m.updateMap(0,0), 5000)