import loginsignupoops     #importing the loginsignup module from the project folder
import distancedataoops    #importing the distance data module from the project folder

class User:    #making a class User containing all the functions for the user 
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role  #basic init function of a class 

    def __str__(self):
        return f"User: {self.username}, Role: {self.role}"  #str function to read the string data of username and password

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Checking if the entered username and password match the admin account
    if username.lower() == "nitanshu tak" and password == "imadmin":
        print("Login successful,welcome Admin.......:)")
        return User(username, password, "admin")
    else:
        print("Login successful,welcome User........:)")
        return User(username, password, "user")  #making the login function

def show_faq():
    print("Frequently Asked Questions:")
    with open("freqaskques.txt", "r") as file:   #opens the frequently asked questions text file from the folder
        faq = file.read()
        print(faq) #making the function to display the frequently asked questions

def connect_social_media():
    print("Connect with us on Instagram on the ID: @realntnsu")
    #making the function to show the social media handle id 

def main():
    print("*" * 40)
    print("Welcome to Flight Ticket Management System") #welcome message in the main function
    print("*" * 40)

    # Log in the user and determine role
    user = login()
    if user.role == "admin":
        print(f"Welcome, {user.username} (Admin)!")
        loginsignupoops.admin_menu()
        #if the entered credentials match the admin account it will open the admin panel
    else:
        print(f"Welcome, {user.username} (User)!")
        user_panel()
        #if the entered credentials does not match admin account, it will automatically open the user panel

def user_panel():
    from flightmatrixoops import main as display_flight_matrix
    # Importing the flightmatrixoops module to use the main function of displaying the flight matrix
    print("What would you like to do?")
    print("1. Book a Flight")
    print("2. Check Airport Connectivity")
    print("3. Social Media Connection")
    print("4. Frequently Asked Questions")
    print("5. Logout (User)")

    while True:
        choice = input("Enter your choice (1/2/3/4/5): ") #making a menu driven program for the user options 

        if choice == "1":
            display_flight_matrix()  # Calling the main function of fligtmatrixoops to display flight matrix
            book_flight()
        elif choice == "2":
            check_airport_connectivity()    #calling the main function from the distancedataoops module to access connectivity map
        elif choice == "3":
            connect_social_media()   #calling the function to show the social media handle
        elif choice == "4":
            show_faq()       #calling the function to show the frequently asked qiestions
        elif choice == "5":
            print("Logging out (User)...")
            break    #this options loggs the user out of the program 
        else:
            print("Invalid choice, please try again..........:(")  #only in the case if user enters anything other than 1/2/3/4/5


def book_flight():
    print("Available flights:")
    from flightmatrixoops import FlightMatrix

    try:
        import flightmatrixoops
    except ImportError:
        print("Error: Flight Matrix cannot be accessed, module not found.")
        return     #adding exceptional handling for the case of importing the flightmatrixoops module

    flightno = input("Enter the flight number you want to book: ")
    with open("flights.txt", "r") as file:     #opening the text file conataining the flight info
        for line in file:
            flightinfo = line.strip().split(',')
            if flightinfo[0] == flightno:
                dep_city, ar_city, time, price = flightinfo[2], flightinfo[3], flightinfo[1], flightinfo[4]
                print("*" * 40)
                print(f"Your flight {flightno} from {dep_city} to {ar_city} at {time} with a ticket price of {price} has been successfully booked.")
                print("*" * 40)
                break
        else:
            print("Flight not found, please enter a valid flight number or recheck the availiability......:(")
            #making the function for booking the flight menu


def check_airport_connectivity():
    print("Airport Connectivity Map:")
    distancedataoops.main()  # Calling distancedataoops module  to access the connectivity map of the airport

if __name__ == "__main__":
    main()     #calling the main function 



