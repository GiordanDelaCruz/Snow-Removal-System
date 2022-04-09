# -*- coding: utf-8 -*-


import requests
import json

class Weather:
    
    def __init__(self, city, country):
        self.city = city
        self.country = country
        self.latitude = 0
        self.longitude = 0
        self.weather = ''
        self.initialize()
        print("The weather in {}: {}".format(self.city, self.weather))
    def get_coords(self):        
    #use weather api to get latitude and longtiude of toronto and store those values    
        response = requests.get(
            "http://api.openweathermap.org/geo/1.0/direct?q={city},{country}\
            &limit=1&appid=9acbb4e08928a9db7363cebc8a569a00".format(city=self.city, country=self.country)
            )
        data = response.text
        parse_json = json.loads(data)
        self.latitude = parse_json[0]['lat']
        self.longitude = parse_json[0]['lon']
        return self.latitude, self.longitude

    def get_weather(self):
    #use stored latitude and longitude needed to get weather data in weather api call
        response = requests.get(
            "https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=9acbb4e08928a9db7363cebc8a569a00".format(lat=self.latitude,lon=self.longitude)
            )
        data = response.text
        parse_json = json.loads(data)
        self.weather = parse_json['weather'][0]['main']
        return self.weather
    
    def initialize(self):
    #runs get_coords and get_weather so it does not need to be called seperately upon creation of
    #weather object
        self.get_coords()
        self.get_weather()
        
        
tor = Weather("Toronto", "CA")
# print(tor.weather)

