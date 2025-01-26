class UserManagement:                         #here we made a class
    def __init__(self):
        self.usersfile = "users.txt"
        self.flightsfile = "flights.txt"           #def init function in the class

    def sign_up(self):
        username = input("Enter your username: ").strip()
        password = input("Enter your password: ").strip()      #input for username and password
        role = "admin" if username.lower() == "nitanshu tak" and password == "imadmin" else "user"

        with open(self.usersfile, "a") as file:
            file.write(f"{username},{password},{role}\n")
        print("Congratulations....your sign up is successful.......:)")     #function for signup

    def login(self):
        username = input("Enter your username: ").strip()
        password = input("Enter your password: ").strip()

        if username.lower() == "nitanshu tak" and password == "imadmin":
            print("Admin login successful........:)")
            return "admin"
        else:
            with open(self.usersfile, "r") as file:        #opening the text file storing all the details of everyone signed in
                for line in file:
                    data = line.strip().split(',')
                    if len(data) == 3:
                        storedusername, storedpassword, role = data
                        if username == storedusername and password == storedpassword: #checking if password and username match 
                            print("User login successful.......:)")
                            return role.strip().lower()

        print("Invalid username or password, please try again.......:(")
        return None                  #function for log in process 

def updtticketprice():
    flightname = input("Enter the name of flight: ")
    newprice = input("Enter the new ticket price (add $ in front): ")

    with open("flights.txt", "r") as file:
        lines = file.readlines()

    with open("flights.txt", "w") as file:      #opening the file conatining all the flight information
        for line in lines:
            if flightname in line:
                flightinfo = line.strip().split(',')
                flightinfo[-1] = newprice
                line = ",".join(flightinfo) + "\n"
            file.write(line)

    print("The ticket price has been updated successfully.......:)")  #function for updating the ticket prices

def dltflights():
    flightname = input("Enter the flight name to be deleted: ")

    with open("flights.txt", "r") as file:
        lines = file.readlines()

    with open("flights.txt", "w") as file:
        for line in lines:
            if flightname not in line:
                file.write(line)

    print("The flight has been deleted successfully.......:)")  #function to delete any flights from the databse

def rescheduleflight():
    flightname = input("Enter the flight name you want to reschedule: ")
    newtime = input("Enter the new departure time of the flight: ")

    with open("flights.txt", "r") as file:
        lines = file.readlines()

    with open("flights.txt", "w") as file:
        for line in lines:
            if flightname in line:
                flightinfo = line.strip().split(',')
                flightinfo[1] = newtime
                line = ",".join(flightinfo) + "\n"
            file.write(line)

    print("The flight has been rescheduled successfully.......:)")   #function to reschedule all the flights

def dltlocation():
    location = input("Enter the location to be deleted: ")

    with open("flights.txt", "r") as file:
        lines = file.readlines()

    with open("flights.txt", "w") as file:
        for line in lines:
            if location not in line:
                file.write(line)

    print("The location and related flights have been deleted successfully.......:)")  #function to delete locations 

# loginsignupoops.py

def admin_menu():
    print("Admin Menu:")    #making a menu driven program of 5 different options
    while True:             #while true helps in the continuous usage of the loop and at 5 it stops
        print("1. Update Ticket Price")      
        print("2. Delete Flight")
        print("3. Reschedule Flight")
        print("4. Delete Location")
        print("5. Exit Admin Menu")
        choice = input("Enter your choice from above (1/2/3/4/5): ")
        if choice == "1":
            updtticketprice()     #calling the function to update price
        elif choice == "2":
            dltflights()          #calling the function to delete flights
        elif choice == "3":
            rescheduleflight()    #calling the function to reschedule flights
        elif choice == "4":
            dltlocation()         #calling the function to delete locations
        elif choice == "5":
            print("Exiting The Admin Menu....")   #ends program
            break
        else:
            print("That's an invalid choice, please try again........:)")   #only when the user enters anything other than 1/2/3/4/5 

if __name__ == "__main__":
    main()
    main()   #calling the main function
