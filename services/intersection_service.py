from services.request_density_service import RequesDesity

import csv
import random

class IntersectionService:
    def __init__(self, csv_file):
        self.intersections = self.load_intersections_from_csv(csv_file)

    def load_intersections_from_csv(self, file_path):
        intersections = []
        with open(file_path, 'r') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            for row in csv_reader:
                intersection = {
                    'id': int(row['id']),
                    'longitude': float(row['longitude']),
                    'latitude': float(row['latitude'])
                }
                intersections.append(intersection)
        return intersections

    def generate_random_origins_destinations(self,num_pairs, current_hour):
        pairs = []
        ids = []  # Lista para almacenar los IDs de las intersecciones seleccionadas
        density = RequesDesity(num_pairs)
        num_pairs =density.perform_action_based_on_hour(current_hour)
        for _ in range(num_pairs):
            origin = random.choice(self.intersections)
            destination = random.choice(self.intersections)
            pairs.append({
                'origin_lat': origin['latitude'],
                'origin_lng': origin['longitude'],
                'destination_lat': destination['latitude'],
                'destination_lng': destination['longitude']
            })
            # Agregar los IDs de las intersecciones seleccionadas a la lista
            ids.append((origin['id'], destination['id']))
        return pairs, ids

