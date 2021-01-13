from collections import namedtuple

from service.traffic_api import get_all_traffic_forecasts
from service.traffic_forecast import TrafficForecast


def get_forecast_by_hour(selected_hour: str) -> TrafficForecast:
    """Return a Forecast object for a given hour.
    TODO: each call to the method call the api, this can be optimized
    """
    forecasts_list = get_all_traffic_forecasts()
    for forecast in forecasts_list:
        if str(forecast.timestamp.hour) == selected_hour:
            return forecast


Metric = namedtuple("Metric", ["minimum", "maximum", "average"])


def get_metrics() -> Metric:
    forecasts_list = get_all_traffic_forecasts()
    minimum = min(forecasts_list)
    maximum = max([forecast.vehicles_count for forecast in forecasts_list])
    average = sum([forecast.vehicles_count for forecast in forecasts_list]) / len(
        forecasts_list
    )
    return Metric(minimum, maximum, average)
