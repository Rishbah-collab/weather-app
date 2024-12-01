import requests
from django.shortcuts import render
from .forms import CityForm

def get_weather(request):
    api_key = 'cd202b2df68d0a02df47fe3623bc3583'
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric'
    weather_data = {}
    
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            response = requests.get(url.format(city, api_key)).json()
            if response['cod'] == 200:  # Check if city exists
                weather_data = {
                    'city': response['name'],
                    'temperature': response['main']['temp'],
                    'description': response['weather'][0]['description'],
                    'icon': response['weather'][0]['icon'],
                    'humidity': response['main']['humidity'],
                    'wind_speed': response['wind']['speed'],
                    'pressure': response['main']['pressure'],
                }
    else:
        form = CityForm()

    return render(request, 'weather/weather.html', {'form': form, 'weather_data': weather_data})

