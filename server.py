import http.client
import json

class handler:
    
    def do_GET(self):
        conn = http.client.HTTPConnection("103.215.208.107", 8585)
        headers = {'Content-type': 'application/json'}
        conn.request("GET", "/geoserver/aasdagrometgis/wms?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetFeatureInfo&TRANSPARENT=true&QUERY_LAYERS=%09aasdagrometgis%3ACrop_advisory_regional&LAYERS=%09aasdagrometgis%3ACrop_advisory_regional&tiled=true&INFO_FORMAT=application%2Fjson&FEATURE_COUNT=999&propertyName=custom_date%2Cdistrict_name%2Ccrop_name%2Cadvisory_reg&I=0&J=2&WIDTH=256&HEIGHT=256&CRS=EPSG%3A4326&STYLES=&BBOX=28.125%2C77.34375%2C29.53125%2C78.75", headers=headers)
        response = conn.getresponse()
        data = response.read()
        # Parse the response as JSON
        json_data = json.loads(data)
        # Send the response to the client
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        # Generate HTML code for each advisory and display as individual cards
        html = ""
        for feature in json_data["features"]:
            crop_name = feature["properties"]["crop_name"]
            advisory_reg = feature["properties"]["advisory_reg"]
            html += f'<div class="card"><h3 class="card-title">{crop_name}</h3><div class="card-body"><p class="card-text">{advisory_reg}</p></div></div>'
        self.wfile.write(bytes(html, "utf-8"))
