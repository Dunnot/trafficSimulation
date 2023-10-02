from datetime import datetime
import os
class ServiceLogger:
    def __init__(self, path):
        self.log_filename = path
        os.makedirs(self.log_filename, exist_ok=True)

    def log_request(self, error_message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"[{timestamp}] Error: {error_message}\n"
        filepath = os.path.join(self.log_filename, "log_request.txt")
        try:
            with open(filepath, 'a') as log_file:
                log_file.write(log_message)
        except Exception as e:
            print("Error al guardar el registro:", str(e))
