import requests

def get_weather(city):
    api_key = 'your_api_key'
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    return data['weather'][0]['description'], data['main']['temp']

print(get_weather('Singapore'))
