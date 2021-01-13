from typing import List

import requests

from service.traffic_forecast import TrafficForecast
from settings import API_URL


def get_all_traffic_forecasts() -> List[TrafficForecast]:
    raw_result = requests.get(API_URL)
    if raw_result.status_code == 500:
        # todo error handler
        print("ERROR IN API TRAFFIC FORECAST")

    data = raw_result.json()["records"]
    # TODO : LIST TYPAGE ERROR : weird
    forecasts: List[TrafficForecast] = []
    for raw_forecast in data:
        forecasts.append(TrafficForecast(raw_forecast["fields"]))

    return forecasts
