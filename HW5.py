import requests
import pandas as pd
from numpy import average

url = "https://api.open-meteo.com/v1/forecast"
params = {
	"latitude": 50,
	"longitude": 30,
	"hourly": ["temperature_2m", "wind_speed_10m"]
}
response = requests.get(url, params=params)
data = response.json()
df = pd.DataFrame(data["hourly"])
print(df.to_string(index=False))

print("MIN temperature:", min(data["hourly"]["temperature_2m"][:24*3]), "C")
print("MAX temperature:", max(data["hourly"]["temperature_2m"][:24*3]), "C")
print("AVG temperature:", average(data["hourly"]["temperature_2m"][:24*3]), "C")

avg_wind = average(data["hourly"]["wind_speed_10m"][:24*3])
wind_hours = 0
for i in data["hourly"]["wind_speed_10m"]:
    if i > avg_wind:
        wind_hours +=1
print("Hours when wind > avg_wind:", wind_hours, "hours")