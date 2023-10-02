import random
from services.request_density_service import RequesDesity

class ScheduleService:
    def __init__(self, num_base_requests_per_hour, current_hour):
        density = RequesDesity(num_base_requests_per_hour)
        self.num_requests_per_hour = density.perform_action_based_on_hour(current_hour)

    def generate_random_schedule(self):
        return [random.randint(0, 59) for _ in range(self.num_requests_per_hour)]

