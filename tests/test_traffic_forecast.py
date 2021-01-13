from datetime import datetime

from service.traffic_forecast import TrafficForecast

FAKE_RAW_FORECAST = {
    "bm_prevision": 313,
    "bm_refdense": 470,
    "bm_reffluid": 373,
    "bm_heure": "2021-01-13T20:30:00+00:00",
    "bm_cdate": "2011-06-09",
    "bm_ident": 257,
    "bm_gid": 186,
    "bm_mdate": "2021-01-13T14:32:39+00:00",
    "bm_refexcep": 796,
}


def test_weather_traffic_should_init_properly():
    forecast = TrafficForecast(FAKE_RAW_FORECAST)
    assert isinstance(forecast.timestamp, datetime)
    assert forecast.vehicles_count == FAKE_RAW_FORECAST["bm_prevision"]


def test_traffic_forecast_to_dict():
    forecast = TrafficForecast(FAKE_RAW_FORECAST)
    data = forecast.to_dict()
    assert isinstance(data, dict)
    assert data["vehicles_count"] == FAKE_RAW_FORECAST["bm_prevision"]
