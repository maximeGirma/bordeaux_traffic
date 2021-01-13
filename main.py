from math import ceil

from service.traffic_api import get_all_traffic_forecasts
from service.traffic_service import get_forecast_by_hour, get_metrics


def main():
    hour = input("please enter an hour : ")
    forecast = get_forecast_by_hour(str(hour))
    print(f"Prevision for the hour is {forecast.vehicles_count}.")
    metrics = get_metrics()
    print(f"minimum for today is : {metrics['minimum']}")
    print(f"maximum for today is : {metrics['maximum']}")
    print(f"average for today is : {ceil(metrics['average'])}")


if __name__ == "__main__":
    main()
