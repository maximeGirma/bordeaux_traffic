from service.traffic_api import get_all_traffic_forecasts
from service.traffic_forecast import TrafficForecast


def get_forecast_by_hour(selected_hour: str) -> TrafficForecast:
    forecasts_list = get_all_traffic_forecasts()
    for forecast in forecasts_list:
        if str(forecast.timestamp.hour) == selected_hour:
            return forecast


def get_metrics():
    forecasts_list = get_all_traffic_forecasts()
    minimum = min([forecast.vehicles_count for forecast in forecasts_list])
    maximum = max([forecast.vehicles_count for forecast in forecasts_list])
    average = sum([forecast.vehicles_count for forecast in forecasts_list]) / len(
        forecasts_list
    )
    return {
        "minimum": minimum,
        "maximum": maximum,
        "average": average,
    }
