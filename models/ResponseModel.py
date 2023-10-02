class Response:
    def __init__(self, success, data=None, error_message=None):
        self.success = success
        self.data = data
        self.error_message = error_message

    def get_data(self):
        return self.data

    def is_successful(self):
        return self.success
    
    def get_error_message(self):
        return self.error_message