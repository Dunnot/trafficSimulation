import os
import json
from datetime import datetime

class ResponseSaver:
    def __init__(self, output_dir):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def save_response(self, origin_id, destination_id, response_data):
        # Obtener la fecha y hora actual
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"{origin_id}_{destination_id}_{timestamp}_response.json"
        filepath = os.path.join(self.output_dir, filename)

        try:
            with open(filepath, 'w') as json_file:
                json.dump(response_data, json_file)
        except Exception as e:
            print(f"Error saving the response for {origin_id} to {destination_id}: {str(e)}")