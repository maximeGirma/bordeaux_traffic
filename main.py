from service.traffic_api import get_all_traffic_forecasts
from service.traffic_service import get_forecast_by_hour


def main():
    hour = input("please enter an hour : ")
    forecast = get_forecast_by_hour(str(hour))
    print(f"Prevision for the hour is {forecast.vehicles_count}.")



if __name__ == "__main__":
    main()
