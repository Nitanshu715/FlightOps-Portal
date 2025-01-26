import loginsignup
def main():
    print("*" * 40)
    print("___Welcome to Flight Ticket Management System___")
    print("*" * 40)
    signlog= input("Do you want to sign up or login? (signup/login): ")
    if signlog=="signup":
        loginsignup.sign_up()
        role=input("Enter your role:(admin/user)=")
        if role=="admin":
            print("Welcome to Admin Panel")
            loginsignup.admin_menu() # Here calling admin_menu function from loginsignup module
        elif role == "user":
            print("Welcome to User Panel")
            task = input("What would you like to do?\n1. Book a flight\n2. Check airport connectivity map\nEnter your choice (1/2): ")
            print(task)
            if task=="1":
                print("Available flights:")
                import flightmatrix
                flightno= input("Enter the flight number you want to book: ")
                with open("flights.txt", "r") as file:
                    for i in file:
                        flightinfo=i.strip().split(',')
                        if flightinfo[0]==flightno:
                            depcity,arcity,time,price=flightinfo[2],flightinfo[3],flightinfo[1],flightinfo[4]
                            break
                    else:
                        print("Flight not found, please enter a valid flight number :)")
                        return  # Exit the function if flight is not found in the matrix
                print("*" * 40)
                print(f"Your flight {flightno} from {depcity} to {arcity} at {time} with a ticket price of {price} has been successfully booked :)")
                print("*" * 40)
            elif task=="2":
                print("Airport Connectivity Map:")
                import distancedata
                distancedata.main()
                print("*" * 40)
                print("Thank you for choosing us!!!!!!")
                print("*" * 40)
            else:
                print("Invalid choice :(")
        else:
            print("Invalid role, exiting program.....")
    else:
        print("Invalid option :(")

main()

def showfaq():
    print("Frequently Asked Questions:")
    with open("freqaskques.txt", "r") as file:     #function to show frequently asked questions
        faq=file.read()
        print(faq)
        
def connectsm():
    print("Connect with us on Instagram: @realntnsu")  #function to ask about social media connection

def main2():
    while True:
        print("What do you want to know now?")
        print("1. Frequently Asked Questions")
        print("2. Connect to our Social Media")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")
        
        if choice=="1":
            showfaq()
        elif choice=="2":
            print("*" * 40)
            connectsm()
            print("*" * 40)
            break
        elif choice=="3":
            print("*" * 40)
            print("Exiting program..... Have a great day :)")
            print("*" * 40)
            break
        else:
            print("Invalid choice :( ")

main2()






