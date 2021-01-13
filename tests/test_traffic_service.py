from service.traffic_forecast import TrafficForecast
from service.traffic_service import get_forecast_by_hour


def test_get_forecast_by_hour():
    assert isinstance(get_forecast_by_hour(str(5)), TrafficForecast)
