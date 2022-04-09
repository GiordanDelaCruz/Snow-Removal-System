import directions as dir
import weather as wea

def check_weather(weather):
    if(weather == "Snow"):
        create_vehicle_routes()
    else:
        return "The weather is currently {} and no operation needs to be done".format(weather)      
            
def create_vehicle_routes():

 origin = "Agincourt+North+Scarborough+Toronto+ON"
 
 # Read neighbourhoods in text file
 with open("n.txt") as f:
     neighbors = f.readlines()
 
 count = 0
 # Strips the newline character
 for n in neighbors:
     count += 1
     destination = n.strip()
     directionObj = dir.Directions(origin, destination)
     print("\nZone{}: {}".format(count, n.strip()))
     route = directionObj.get_route()
     directionObj.print_route(route)
     print("\nThe ETA is: {}".format(directionObj.get_ETA()))



check_weather('Snow')