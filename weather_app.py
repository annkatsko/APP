import requests
import json

learn_weather = True
while learn_weather:
    while True:
        city = input('Type your city: ')
        api_key = 'a488843f82be53b9e7cd32ac32efc685'
        url = 'https://api.openweathermap.org/data/2.5/weather'
        data = requests.get(url, params = {'q' : city, 'appid': api_key}).json()
        print('Temperature in ' + city + ' is ' + str(round(data['main']['temp']-273.15)) + '°С.')
        quastion = input('Would you like to learn weather in another city? Type yes or no. ').lower()
        if quastion == 'no':
            learn_weather = False
            print('Thanks for using our app!')
            break