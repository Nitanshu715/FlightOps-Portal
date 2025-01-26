def rdist(filename):
    distances={}
    with open(filename,"r") as file:
        next(file)
        for i in file:            #it opens the distances.txt file and iterates 
            if i.strip():       #i itrates through each element from the file
                data=i.strip().split(',')
                if len(data)>=2:    #elements are accessed based on distance and location  
                    location,distance=data
                    distances[location.strip().capitalize()]=int(distance)
                else:
                    print(f"Ignoring line: {i}")
    return distances

def main():
    filename="distances.txt"
    distances=rdist(filename)
    print("Entries in the database:")
    for location,distance in distances.items(): #checks distance elements for location and distance 
        print(f"{location}: {distance} km")
    destination=input("Where do you wanna go? Please enter the location:").strip().capitalize()
    if destination in distances:
        distance=distances[destination]
        print(f"The distance to {destination} from the airport is {distance} Km")
        if distance<4:
            print("You can pick a taxi from Gate 1 :)")
        else:
            print("You can pick a taxi from Gate 2 :)")
    else:
        print("Sorry, the destination is not found in the database :(")
