class TransportationSystem:              #making a parent class
    def __init__(self, filename):
        self.filename = filename        #making the basic init function of a class

    def readdata(self):
        print("Warning: Subclasses should implement 'readdata' method to read data from a file.")
        #declaring the function to read data in the parent class which must be implemented to read the file data

    def displayinfo(self):
        print("Warning: Subclasses should implement 'displayinfo' method to display information.")
        #declaring the information displaying function

    def finddestination(self, destination):
        print(f"Warning: Subclasses should implement 'finddestination' method to find '{destination}'.")
        #declaring the destination searching function which will only run when implemented in the subclass


class Distance(TransportationSystem):     #making the child class distance
    def __init__(self, filename):
        super().__init__(filename)
        self.distances = {}

    def readdata(self):
        with open(self.filename, "r") as file:
            next(file)
            for line in file:
                if line.strip():
                    data = line.strip().split(',')
                    if len(data) >= 2:
                        location, distance = data
                        self.distances[location.strip().capitalize()] = int(distance)
                    else:
                        print(f"Ignoring line: {line}")   #read data function to read the data from distances.txt

    def displayinfo(self):
        print("Locations in the database:")
        for location, distance in self.distances.items():
            print(f"{location}: {distance} km")    #this displays all the locations from the database along with there distances

    def finddestination(self, destination):
        if destination in self.distances:
            distance = self.distances[destination]
            print(f"The distance to {destination} from the airport is {distance} Km")
            if distance < 4:
                print("You can pick the taxi from Gate 1 :)")
            else:
                print("You can pick the taxi from Gate 2 :)")
        #based on the distance of the selected location from the airport it suggests the best taxi route to be picked from which gate
        else:
            print("Sorry, the destination you entered cannot be found in the database.........:(")


def main():
    filename = "distances.txt"
    data = Distance(filename)
    data.readdata()
    data.displayinfo()
    destination = input("Where do you wanna go? Please enter the location: ").strip().capitalize()
    data.finddestination(destination)
#here we store the distances.txt file in the filename variable, and call the functions

if __name__ == "__main__":
    main() #calling main function main()
