import directions as dir
import weather as wea

def create_dictionaries():
    directions = {}
    eta = {}
    origin = "Agincourt+North+Scarborough+Toronto+ON"
    # Read neighbourhoods in text file
    with open("ntest.txt") as f:
        neighbors = f.readlines()
    for n in neighbors:
        destination = n.strip()
        directionObj = dir.Directions(origin, destination)
        route = directionObj.get_route()
        directions.update({destination : route})
        eta[destination] = directionObj.get_ETA()
    return [directions, eta]
    
    
    # return directions, eta
            
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




# ist = create_dictionaries()
# print(ist[1]["Agincourt North"])