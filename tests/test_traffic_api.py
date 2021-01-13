from service.traffic_api import get_all_traffic_forecasts
from service.traffic_forecast import TrafficForecast


def test_traffic_api():
    forecast_list = get_all_traffic_forecasts()
    assert forecast_list
    for forecast in forecast_list:
        assert isinstance(forecast, TrafficForecast)
