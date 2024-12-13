import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_weather(city: str) -> str:

    API_NINJAS_API_KEY=os.getenv('API_NINJAS_API_KEY')

    # First get the latitude and longitude of the city
    api_url = 'https://api.api-ninjas.com/v1/city?name={}'.format(city)
    response = requests.get(api_url, headers={'X-Api-Key': API_NINJAS_API_KEY})
    lat = response.json()[0]['latitude']
    lon = response.json()[0]['longitude']

    # Now get the weather
    api_url = f'https://api.api-ninjas.com/v1/weather?lat={lat}&lon={lon}'
    response = requests.get(api_url, headers={'X-Api-Key': API_NINJAS_API_KEY})
    temp = response.json()['temp']

    return temp

if __name__ == '__main__':
    city = 'Zagreb'
    temp = get_weather(city)
    print(f'Temperature in {city} is {temp} degrees Celsius')