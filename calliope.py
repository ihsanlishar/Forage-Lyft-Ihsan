from datetime import datetime
from engine.capulet_engine import CapuletEngine

class Calliope(CapuletEngine):
    def needs_service(self):
        return self._time_or_engine_based_service_check(2)

    def _time_or_engine_based_service_check(self, years):
        return self.time_based_service_check(years) or super().needs_service()
