import directions as dir
import weather as wea


def main():
    # Runnging Test Classes
    testWeather()
    testDirections()

   

def testWeather():
    # Testing weather class
    print("*********       Testing Weather Class      ***********\n")
    city = "Toronto"
    country = "CA"
    weatherObj = wea.Weather(city, country)
    print("Weather in {}: {}".format(city, weatherObj.weather))

def testDirections():
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

    # print("From {} to {}:\n".format(origin, destination))
    # pretty_text = directionsObj.get_pretty_route()
    # directionsObj.print_route(pretty_text)

main()
