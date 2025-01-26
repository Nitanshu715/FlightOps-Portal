cities=["New York","London","Tokyo","Paris","Sydney","Mumbai","Rio de Janeiro","Beijing","Berlin","Cape Town"]
flmatrix={}         #after making a list of cities, an empty dictionary is created
for depcity in cities:
    flmatrix[depcity]={}  #nested loop to itrate each city with all other cities
    for arcity in cities:
        if depcity!=arcity:
            flmatrix[depcity][arcity]=[]
file_path="C:/Users/nitan/OneDrive/Desktop/python/project/flights.txt"
with open(file_path,"r") as file:
    next(file)
    for i in file:
        flightinfo=i.strip().split(',')
        if len(flightinfo)>=4:      #info with all things name,boarding city, arrival city, price, time
            depcity=flightinfo[2]
            arcity=flightinfo[3]
            fldetails=",".join(flightinfo[:2]+flightinfo[4:])
            flmatrix[depcity][arcity].append(fldetails) #appends all together
for depcity,arcities in flmatrix.items():
    print(f"Flights from {depcity}:")
    for arcity,flights in arcities.items():  #nested loop again to show 1 city to all cities 
        print(f"...To {arcity}:")
        if flights:
            for flight in flights:
                print(f"......{flight}")
        else:
            print(".........No flights available for this route :(")

