class FlightMatrix:                #making the flightmatrix class
    def __init__(self, cities, file_path):
        self.flmatrix = {}
        self.cities = cities
        self.file_path = file_path   #making the basic init function of a class

    def buildflightmatrix(self):
        for depcity in self.cities:
            self.flmatrix[depcity] = {}
            for arcity in self.cities:
                if depcity != arcity:
                    self.flmatrix[depcity][arcity] = []
        #this function helps in building the matrix and integrates all the flight info

        try:
            with open(self.file_path, "r") as file:
                next(file)  # Skip the header line
                for line in file:
                    flightinfo = line.strip().split(',')
                    if len(flightinfo) >= 4:
                        depcity = flightinfo[2]
                        arcity = flightinfo[3]
                        fldetails = ",".join(flightinfo[:2] + flightinfo[4:])
                        self.flmatrix[depcity][arcity].append(fldetails)
        except FileNotFoundError:
            print(f"Error: File not found at path '{self.file_path}'")
        except StopIteration:
            print("Warning: No valid flight data found in the file")
#using exceptional handling to open the file and if it not open ,this print statement will be shown instead of the file not found error

    def displayflightmatrix(self):
        for depcity, arcities in self.flmatrix.items():
            print(f"Flights from {depcity}:")
            for arcity, flights in arcities.items():
                print(f"...To {arcity}:")
                if flights:
                    for flight in flights:
                        print(f"......{flight}")
                else:
                    print(".........No flights available for this route :(") #function to show the matrix integrating the info

def main():
    cities = ["New York", "London", "Tokyo", "Paris", "Sydney", "Mumbai", "Rio de Janeiro", "Beijing", "Berlin", "Cape Town"]
    file_path = "C:/Users/nitan/OneDrive/Desktop/python/project/flights.txt"

    # Create a variable of FlightMatrix
    flight_matrix = FlightMatrix(cities, file_path)

    # Build the flight matrix and calling build flight matrix function
    flight_matrix.buildflightmatrix()

    # Display the flight matrix using the display flight matrix function 
    flight_matrix.displayflightmatrix()

if __name__ == "__main__":
    main()  # Call the main function to start the program

