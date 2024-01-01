from datetime import datetime
from engine.willoughby_engine import WilloughbyEngine

class Rorschach(WilloughbyEngine):
    def needs_service(self):
        return self._time_or_engine_based_service_check(4)

    def _time_or_engine_based_service_check(self, years):
        return self.time_based_service_check(years) or super().needs_service()
