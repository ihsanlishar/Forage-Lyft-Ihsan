from car import Car

class CapuletEngine(Car):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        super().__init__(last_service_date)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        return self._time_or_mileage_based_service_check(2)

    def _time_or_mileage_based_service_check(self, years):
        mileage_threshold = 30000
        return self.time_based_service_check(years) or (
            self.current_mileage - self.last_service_mileage > mileage_threshold
        )
