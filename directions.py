import requests
import json
from helper import cleanhtml
import config

#directions api key
apiKey= config.api_direction_key

class Directions:
    
    def __init__(self, origin, destination):
        self.origin = origin
        self.destination = destination
        self.tagged_route = []
        self.route = []
        self.ETA = ''
        self.initialize()

    def initialize(self):
        #create the route from origin to destination
        self.set_tagged_route()
        self.remove_html_tags()
        self.calculate_ETA()

    def set_tagged_route(self):        
    #update values found in route 
        response = requests.get(
            "https://maps.googleapis.com/maps/api/directions/json?origin={origin}&destination={destination}&key={APIkey}".format(origin=self.origin, destination = self.destination, APIkey = apiKey)
            )
        data = response.text
        parse_json = json.loads(data)
        query = parse_json['routes'][0]['legs'][0]["steps"]
        for i in range(0, len(query)):
            self.tagged_route.append(query[i]["html_instructions"])
    
    def get_tagged_route(self):
    #return the route WITH HTML tags
        return self.route

    def remove_html_tags(self):
    #remove html tags found in route 
        for i in range(0, len(self.tagged_route)):
            text = cleanhtml(self.tagged_route[i])
            self.route.append(text)

    def get_route(self):
    #return the route WITHOUT HTML tags
        return self.route

    def calculate_ETA(self):
    #calculate the ETA from origin to desitination
        response = requests.get(
            "https://maps.googleapis.com/maps/api/directions/json?origin={origin}&destination={destination}&key={APIkey}".format(origin=self.origin, destination = self.destination, APIkey = apiKey)
            )
        data = response.text
        parse_json = json.loads(data)
        self.ETA = parse_json['routes'][0]['legs'][0]["duration"]["text"]
        
    def get_ETA(self):
    #return the ETA from origin to destination
        return self.ETA

    def print_route(self, route_list):
    #print out values inside list
       for i in range(0, len(route_list)):
            print(route_list[i])


#--------------------------------------------------------------------------------------------
#--                             TESTING & DEBUGGING                                        --
#--------------------------------------------------------------------------------------------
def main():
    origin = "99 Wellesley St W, Toronto, ON" 
    destination = "Agincourt North Scarborough, Toronto ON" 
    directionsObj = Directions(origin, destination)

    # tagged_text = directionsObj.get_tagged_route()
    # directionsObj.print_route(tagged_text)

    # clean_text = directionsObj.get_route()
    # directionsObj.print_route(clean_text)

    ETA = directionsObj.get_ETA()
    print("From {} to {};\nETA: {}\n".format(origin, destination, ETA))

# main()



