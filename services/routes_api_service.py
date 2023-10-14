import requests
import json
from models.ResponseModel import Response

class RouteAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://routes.googleapis.com/directions/v2:computeRoutes'

    def make_api_request(self, origin_lat, origin_lng, destination_lat, destination_lng):
        headers = {
            'Content-Type': 'application/json',
            'X-Goog-Api-Key': self.api_key,
            'X-Goog-FieldMask': 'routes.duration,routes.distanceMeters,routes.legs.polyline,routes.legs.travelAdvisory,routes.legs.steps.polyline,routes.legs.steps.distanceMeters,routes.legs.steps.staticDuration,routes.legs.startLocation,routes.legs.endLocation'
        }

        data = {
            "origin": {
                "location": {
                    "latLng": {
                        "latitude": origin_lat,
                        "longitude": origin_lng
                    }
                }
            },
            "destination": {
                "location": {
                    "latLng": {
                        "latitude": destination_lat,
                        "longitude": destination_lng
                    }
                }
            },
            "travelMode": "DRIVE",
            "units": "METRIC",
            "languageCode": "es-CO",
            "extraComputations": ["TRAFFIC_ON_POLYLINE"],
            "routingPreference": "TRAFFIC_AWARE",
            "polylineEncoding": "GEO_JSON_LINESTRING"
        }
        try:
            response = requests.post(self.base_url, headers=headers, data=json.dumps(data))
            if response.status_code == 200:
                response_json = response.json()
                return Response(success=True, data=response_json)
            else:
                error_message = f"Error in API request. Status code: {response.status_code}"
                return Response(success=False, error_message=error_message)
        except requests.exceptions.RequestException as e:
            error_message = f"Error in API request. Status code: {e}"
            return Response(success=False, error_message=error_message)
