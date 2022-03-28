import requests
import json
from helper import *
import config

#directions api key
apiKey= config.api_direction_key

class Directions:
    
    def __init__(self, origin, destination):
        self.origin = origin
        self.destination = destination
        self.route = []
        self.pretty_route = []
        self.initialize()

    def initialize(self):
        #create the route from origin to destination
        self.set_route()
        self.set_pretty_route()

    def set_route(self):        
    #update values found in route 
        response = requests.get(
            "https://maps.googleapis.com/maps/api/directions/json?origin={origin}&destination={destination}&key={APIkey}".format(origin=self.origin, destination = self.destination, APIkey = apiKey)
            )
        data = response.text
        parse_json = json.loads(data)
        query = parse_json['routes'][0]['legs'][0]["steps"]
        for i in range(0, len(query)):
            self.route.append(query[i]["html_instructions"])
    
    def get_route(self):
    #read the values found in route
        return self.route

    def set_pretty_route(self):
    #update prettier values  found in route 
        for i in range(0, len(self.route)):
            text = cleanhtml(self.route[i])
            self.pretty_route.append(text)

    def get_pretty_route(self):
    #read the prettier values found in route
        return self.pretty_route

    def print_route(self, route_list):
    #print out values inside list
       for i in range(0, len(route_list)):
            print(route_list[i])

#--------------------------------------------------------------------------------------------
#--                             TESTING & DEBUGGING                                        --
#--------------------------------------------------------------------------------------------
def main():
    origin = "Agincourt+North+Scarborough+Toronto+ON"
    destination = "24+Sussex+Drive+Ottawa+ON"
    tor = Directions(origin, destination)
    pretty_text = tor.get_pretty_route()
    tor.print_route(pretty_text)

main()



