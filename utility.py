import directions as dir
import weather as wea


def create_vehicle_routes():
  # Testing directions class
 print("\n\n*********       Testing Directions Class      ***********\n")
 origin = "Agincourt+North+Scarborough+Toronto+ON"
 
 # Read neighbourhoods in text file
 with open("n.txt") as f:
     neighbors = f.readlines()
 
 count = 0
 # Strips the newline character
 for n in neighbors:
     count += 1
     destination = n.strip()
     dir.Directions(origin, destination)
     print("\nZone{}: {}".format(count, n.strip()))
