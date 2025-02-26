(function($) {
    $(document).ready(function() {
        var $latField = $('#id_latitude');
        var $lngField = $('#id_longitude');

        var map = $('.leaflet-map').data('leaflet-map'); // Получаем карту Leaflet
        if (!map) return;

        var marker = null;

        // Найти существующий маркер или создать новый
        map.eachLayer(function(layer) {
            if (layer instanceof L.Marker) {
                marker = layer;
            }
        });

        if (!marker) {
            var initLat = parseFloat($latField.val()) || 55.7558;  // Москва (по умолчанию)
            var initLng = parseFloat($lngField.val()) || 37.6173;
            marker = L.marker([initLat, initLng], { draggable: true }).addTo(map);
        }

        // Обновление координат при перемещении маркера
        marker.on('dragend', function(event) {
            var latlng = event.target.getLatLng();
            $latField.val(latlng.lat.toFixed(6));
            $lngField.val(latlng.lng.toFixed(6));
        });

        // Обновление маркера при изменении широты и долготы в форме
        function updateMarkerPosition() {
            var lat = parseFloat($latField.val());
            var lng = parseFloat($lngField.val());
            if (!isNaN(lat) && !isNaN(lng)) {
                marker.setLatLng([lat, lng]);
                map.panTo([lat, lng]);
            }
        }

        $latField.on('change', updateMarkerPosition);
        $lngField.on('change', updateMarkerPosition);
    });
})(django.jQuery);
