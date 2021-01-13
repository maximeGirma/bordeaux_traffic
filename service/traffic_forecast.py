from datetime import datetime


class TrafficForecast(object):
    def __init__(self, data: dict):
        self.timestamp = datetime.strptime(data["bm_heure"], "%Y-%m-%d %H:%M:%S.%f")
        self.vehicles_count = data["bm_prevision"]

    def to_dict(self) -> dict:
        data = vars(self)
        data["timestamp"] = str(data["timestamp"])
        return data
