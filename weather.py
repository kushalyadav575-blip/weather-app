import requests
import os
weather_api=os.environ.get("WEATHER_API_KEY")
geo_api=os.environ.get("GEO_CODING_API")
def get_weather(city):

    params={
        "name":city
        }

    try:
        response=requests.get(geo_api,params=params,timeout=5)
        response.raise_for_status()
        data=response.json()
   
        if "results" not in data or not data["results"]:
            print("no such city found")
            return None
        else:
            lat = data["results"][0]["latitude"]
            lon = data["results"][0]["longitude"]

    except requests.exceptions.RequestException:
        print("error encounterd")
        return None


    params={
        "latitude":lat,
        "longitude":lon,
        "current":"temperature_2m",
        "daily":"temperature_2m_max,temperature_2m_min"
        }

    try:
        response=requests.get(weather_api,params=params,timeout=5)
        response.raise_for_status()
        data=response.json()
        current_temp=data["current"]["temperature_2m"]
        temp_unit=data["current_units"]["temperature_2m"]
        time=data["daily"]["time"]
        max_temp=data["daily"]["temperature_2m_max"]
        min_temp=data["daily"]["temperature_2m_min"]

        return {
            "current_temp": current_temp,
            "temp_unit": temp_unit,
            "forecast": [{"date": date, "max": max_t, "min": min_t} for date,max_t,min_t in zip(time[:3],max_temp[:3],min_temp[:3])]
        }

    except requests.exceptions.RequestException:
        print("error encounterd") 
        return None
