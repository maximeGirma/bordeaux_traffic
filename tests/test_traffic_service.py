from service.traffic_forecast import TrafficForecast
from service.traffic_service import get_forecast_by_hour, get_metrics


def test_get_forecast_by_hour():
    assert isinstance(get_forecast_by_hour(str(5)), TrafficForecast)


def test_get_metrics():
    metrics = get_metrics()
    assert metrics.minimum
    assert metrics.maximum
    assert metrics.average
    assert metrics.minimum < metrics.average < metrics.maximum
