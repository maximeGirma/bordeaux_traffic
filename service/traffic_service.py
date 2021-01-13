from service.traffic_api import get_all_traffic_forecasts
from service.traffic_forecast import TrafficForecast


def get_forecast_by_hour(selected_hour: str) -> TrafficForecast:
    forecasts_list = get_all_traffic_forecasts()
    for forecast in forecasts_list:
        if str(forecast.timestamp.hour) == selected_hour:
            return forecast
