class RequesDesity:
    def __init__(self, num_base_requests_per_hour):
        self.num_base_requests_per_hour = num_base_requests_per_hour

    def perform_action_based_on_hour(self, current_hour):
        if 8 <= current_hour < 23:
            num_requests_per_hour = self.num_base_requests_per_hour
            return num_requests_per_hour
        else:
            num_requests_per_hour = self.num_base_requests_per_hour // 5
            return num_requests_per_hour