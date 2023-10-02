import json
import time
import datetime

from services.routes_api_service import RouteAPI
from services.logger_service import ServiceLogger
from services.response_saver_service import ResponseSaver
from services.intersection_service import IntersectionService
from services.generator_schedule_service import ScheduleService

def load_config():
    with open('config/config.json') as config_file:
        return json.load(config_file)


def main():
    config = load_config()
    api_key = config.get('api_key')
    log_path = config.get('log_path')
    responses_path = config.get("responses_path")
    csv_file = config.get("csv_file")
    number_requests_per_hour =config.get("number_requests_per_hour")
    end_date_str = config.get("end_date")
    end_date = datetime.datetime.strptime(end_date_str, "%Y-%m-%d").date()
    sentinel = 0
    random_minutes = []
    pairs = []
    ids = []
    current_time = time.localtime()
    intersections = IntersectionService(csv_file)
    route_api = RouteAPI(api_key)
    previous_minuto = None

    current_hour = current_time.tm_hour
    schedul = ScheduleService(number_requests_per_hour,current_hour)
    random_minutes = schedul.generate_random_schedule()
    pairs, ids = intersections.generate_random_origins_destinations(number_requests_per_hour,current_hour)

    while True:
        current_time = time.localtime()
        current_date = datetime.date(current_time.tm_year, current_time.tm_mon, current_time.tm_mday)

        if current_date > end_date:
            break
        
        if current_time.tm_min == 0 and current_time.tm_min != previous_minuto:
            sentinel = 0
            current_hour = current_time.tm_hour
            schedul = ScheduleService(number_requests_per_hour,current_hour)
            random_minutes = schedul.generate_random_schedule()
            pairs, ids = intersections.generate_random_origins_destinations(number_requests_per_hour,current_hour)
        
        previous_minuto = current_time.tm_min

        if current_time.tm_min in random_minutes:

            for i in range(random_minutes.count(current_time.tm_min)):
                origin_lat, origin_lng = pairs[sentinel]['origin_lat'], pairs[sentinel]['origin_lng']
                destination_lat, destination_lng = pairs[sentinel]['destination_lat'], pairs[sentinel]['destination_lng']

                response = route_api.make_api_request(origin_lat, origin_lng, destination_lat, destination_lng)

                if response.success:
                    origin_id, destination_id = ids[sentinel]  
                    respose_saver = ResponseSaver(responses_path)
                    respose_saver.save_response(origin_id, destination_id, response.data)
                else:
                    service_logger = ServiceLogger(log_path)
                    service_logger.log_request(response.error_message)
                
                sentinel += 1
                random_minutes.remove(current_time.tm_min)


if __name__ == "__main__":
    main()
