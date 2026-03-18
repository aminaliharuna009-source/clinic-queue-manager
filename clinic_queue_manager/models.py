from datetime import datetime
#Patient class representing clinic visitor
class Patient:

    def __init__(self, name):
        self.name = name
        self.time_registered = datetime.now()

    def get_details(self):
        return f"{self.name} (Registered at {self.time_registered.strftime('%H:%M:%S')})"
