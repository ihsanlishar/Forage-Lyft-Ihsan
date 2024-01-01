from abc import ABC, abstractmethod
from datetime import datetime

class Car(ABC):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    @abstractmethod
    def needs_service(self):
        pass

    def time_based_service_check(self, years):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + years)
        return service_threshold_date < datetime.today().date()
