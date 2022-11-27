import requests

API_Key = "bd55ef0ba655cefd16cb35079db9c978"
location = input("Enter Your Desired Location: ")
weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&units=imperial&appid="
final_url = weather_url + API_Key
weather_data = requests.get(final_url).json()
print(weather_data)
from pprint import pprint
pprint(weather_data)
