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
        self.initialize()

    def initialize(self):
        #create the route from origin to destination
        self.set_tagged_route()
        self.remove_html_tags()
        self.print_route(self.get_route())

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
    #read the values found in route
        return self.route

    def remove_html_tags(self):
    #remove html tags found in route 
        for i in range(0, len(self.tagged_route)):
            text = cleanhtml(self.tagged_route[i])
            self.route.append(text)

    def get_route(self):
    #read the cleaner values found in route
        return self.route

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

    # tagged_text = tor.get_tagged_route()
    # tor.print_route(tagged_text)
    # tor.print_route(tor.get_route())
    # clean_text = tor.get_route()
    # tor.print_route(clean_text)

main()



