import os
import requests
from dotenv import load_dotenv
from datetime import datetime
from os.path import join


load_dotenv()
api_key = os.getenv("VISUALCROSSING_API_KEY")

def capture_wind_data():
      
      api_key = os.getenv("VISUALCROSSING_API_KEY")

      cities = {
        "Lagoa do Barro" : "Lagoa do Barro do Piauí,BR",
        "Queimada Nova" : "Queimada Nova,BR",
        "Dom Inocêncio" : "Dom Inocêncio,BR",
        "Sento Sé" : "Sento Sé,BR",
        "Chuí" : "Chuí,BR",
        "Santa Vitória do Palmar": "Santa Vitória do Palmar,BR",
        "Casa Nova": "Casa Nova,BR"
      }

      current_date = datetime.today()
      current_date = datetime.today().strftime('%Y-%m-%d')
      wind_data = {}

      for city, location in cities.items():
            
          url = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}/{current_date}/{current_date}?unitGroup=metric&include=days&key={api_key}&contentType=json'
            
          response = requests.get(url)
          try:
            response.raise_for_status()  
            data = response.json()
            
            wind_speed = data['days'][0]['windspeed']  
            wind_direction = data['days'][0]['winddir']
           
            wind_speed_kmh = wind_speed * 3.6
            wind_data[city] = {
                "speed_kmh": round(wind_speed_kmh, 2),
                "direction_degrees": wind_direction
            }
          except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error for {city}: {http_err}")
            wind_data[city] = {"error": str(http_err)}
          except requests.exceptions.JSONDecodeError:
            print(f"Invalid JSON response for {city}")
            wind_data[city] = {"error": "Invalid JSON response"}
          except KeyError:
            print(f"Missing wind data for {city}")
            wind_data[city] = {"error": "Missing wind data"}

      return wind_data

data = capture_wind_data()
print(data)